import base64

from flask import (
    current_app, abort, Blueprint, request, Response, make_response, jsonify
)
from flask_jwt_extended import (
    jwt_required, create_access_token, create_refresh_token, get_raw_jwt,
    jwt_refresh_token_required, get_jwt_identity, decode_token
)
from jwcrypto import jwk, jwe
from app.model import User, UserUtil
from app.database import db


bp = Blueprint('auth', __name__, url_prefix='/auth')
u = UserUtil()


@bp.route('/register', methods=('POST',))
def register() -> Response:
    if not request.is_json:
        abort(400)

    is_invalid = u.is_invalid(request.json)

    if not is_invalid:
        user = User(email=request.json.get('email'), password=request.json.get('password'))
        db.session.add(user)
        db.session.commit()

        response = make_response(jsonify({
            'status': 'success',
            'data': user.serialize()
        }), 200)
    else:
        response = make_response(jsonify({
            'status': 'fail',
            'data': is_invalid
        }), 400)

    return response


@bp.route('/login', methods=('POST',))
def login() -> Response:
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not request.is_json or not email or not password:
        abort(400)

    user = u.authenticate(email, password)
    if not user:
        response = make_response(jsonify({
            'status': 'fail',
            'message': 'Username or Password not valid'
        }), 401)
    else:
        access_token_encoded = create_access_token(identity=user.email)
        refresh_token_encoded = create_refresh_token(identity=user.email)

        decoded_token = decode_token(access_token_encoded)
        jti = decoded_token['jti']

        if user.email not in current_app.jwt_tokenlist:
            current_app.jwt_tokenlist[user.email] = set()

        current_app.jwt_tokenlist[user.email].add(jti)

        response = make_response(jsonify({
            'status': 'success',
            'data': {
                'access_token': access_token_encoded,
                'refresh_token': refresh_token_encoded
            }
        }), 200)

    return response


@bp.route('/refresh', methods=('POST',))
@jwt_refresh_token_required
def refresh() -> Response:
    current_user = get_jwt_identity()
    response = make_response(jsonify({
        'status': 'success',
        'data': {
            'access_token': create_access_token(identity=current_user)
        }
    }), 200)

    return response


@bp.route('/logout', methods=('GET',))
@jwt_required
def logout() -> Response:
    jti = get_raw_jwt()['jti']
    current_app.jwt_blacklist.add(jti)
    return make_response('', 200)


@bp.route('/key', methods=('GET',))
@jwt_required
def get_public_key() -> Response:
    pub_key = current_app.config.get('MY_PUBLIC_KEY')
    return make_response(jsonify({
        'status': 'success',
        'data': {
            'public_key': pub_key
        }
    }), 200)


@bp.route('/decode', methods=('POST',))
@jwt_required
def decode_secret_message() -> Response:
    enc_b64 = request.json.get('encrypted_message')
    enc = base64.b64decode(enc_b64.encode('ascii'))
    private_key = jwk.JWK.from_json(current_app.config.get('MY_PRIVATE_KEY'))
    jwetoken = jwe.JWE()

    try:
        jwetoken.deserialize(enc, key=private_key)
    except Exception:
        return make_response('', 400)

    payload = jwetoken.payload
    response = make_response(jsonify({
        'status': 'success',
        'data': {
            'secret_message': payload.decode('ascii')
        }
    }), 200)

    return response
