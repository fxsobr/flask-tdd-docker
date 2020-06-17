from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)

api = Api(app)

app.config.from_object('sistema.config.DevelopmentConfig')


class Ping(Resource):
    def get(self):
        return {
            'status': 'sucesso',
            'message': 'pong'
        }


api.add_resource(Ping, '/ping')
