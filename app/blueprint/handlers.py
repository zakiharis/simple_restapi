from flask import make_response, jsonify


def register_handler(app):

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({
            'status': 'fail',
            'message': 'bad request'
        }), 400)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({
            'status': 'error',
            'message': 'not Found'
        }), 404)
