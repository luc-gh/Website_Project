# Modelos para base de dados
# Aqui será definida a estrutura do banco de dados

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):  # Modelo para as notas (armazenadas no banco)
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class User(db.Model, UserMixin):  # Modelo para Usuários
    id = db.Column(db.Integer, primary_key=True)  # Chave única
    email = db.Column(db.String(150), unique=True)  # Quantidade máxima de caracteres / cada objeto é único
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))