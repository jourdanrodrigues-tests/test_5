import os

from flask_sqlalchemy import SQLAlchemy

from app import app

app.config.update({
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': os.getenv('DATABASE_URL'),
})

db = SQLAlchemy(app)
