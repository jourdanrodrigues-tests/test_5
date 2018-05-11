from flask import Flask
from flask_cors import CORS
from views import blueprint


flaskApp = Flask(__name__)

CORS(flaskApp)

flaskApp.register_blueprint(blueprint)
