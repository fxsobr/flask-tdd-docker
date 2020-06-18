from flask import Blueprint, request
from flask_restx import Resource, Api

from sistema import db
from sistema.api.models import Usuario


usuarios_blueprint = Blueprint('usuarios', __name__)
api = Api(usuarios_blueprint)


class UsersList(Resource):
    def post(self):
        post_data = request.get_json()
        usuario = post_data.get('usuario')
        email = post_data.get('email')
        db.session.add(Usuario(usuario=usuario, email=email))
        db.session.commit()
        response_object = {
            'mensagem': f'{email} foi adicionado com sucesso!'
        }
        return response_object, 201


api.add_resource(UsersList, '/usuarios')