import os

from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object('sistema.config.DevelopmentConfig')

db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    ativo = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, usuario, email):
        self.usuario = usuario
        self.email = email


class Ping(Resource):
    def get(self):
        return {
            'status': 'sucesso',
            'message': 'pong'
        }


api.add_resource(Ping, '/ping')
