from flask import (
    current_app, abort, Blueprint, request, Response, make_response, jsonify
)
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)
from app.model import UserUtil


bp = Blueprint('account', __name__, url_prefix='/account')
u = UserUtil()


@bp.route('', methods=('GET',))
@jwt_required
def get_account():
    user_identity = get_jwt_identity()
    user = u.get_by_email(user_identity)

    if not user:
        abort(404)

    return make_response(jsonify({
        'status': 'success',
        'data': user.serialize()
    }), 200)


@bp.route('', methods=('PUT',))
@jwt_required
def update_password() -> Response:
    if not request.is_json:
        abort(400)

    user_identity = get_jwt_identity()
    user = u.get_by_email(user_identity)
    if not user:
        abort(404)

    is_invalid = u.is_invalid(request.json, check_user=False)
    if not is_invalid:
        u.update(user, request.json.get('password'))
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


@bp.route('', methods=('DELETE',))
@jwt_required
def delete_account() -> Response:
    user_identity = get_jwt_identity()
    user = u.get_by_email(user_identity)

    if user:
        u.delete(user)
        if user_identity in current_app.jwt_tokenlist:
            for jti in current_app.jwt_tokenlist[user_identity]:
                current_app.jwt_blacklist.add(jti)
        return make_response('', 200)

    abort(404)
