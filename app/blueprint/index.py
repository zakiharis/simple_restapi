from flask import Blueprint


bp = Blueprint('index', __name__, url_prefix='')


@bp.route('/', methods=['GET'])
def index() -> str:
    return "The server is runing!"
