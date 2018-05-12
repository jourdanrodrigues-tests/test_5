import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from .db import db
from .views import blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(blueprint)

app.config.update({
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': os.getenv('DATABASE_URL'),
})

db.init_app(app)
migrate = Migrate(app, db)
