from flask import Blueprint, request, jsonify

index_app = Blueprint('index_app', __name__)


@index_app.route('/')
def hello_world():
    return 'Hello, World!'
