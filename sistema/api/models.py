from sqlalchemy.sql import func
from sistema import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    data_criacao = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, usuario, email):
        self.usuario = usuario
        self.email = email