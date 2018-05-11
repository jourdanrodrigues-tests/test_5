from flask import Blueprint, jsonify

blueprint = Blueprint('views', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello World!'})
