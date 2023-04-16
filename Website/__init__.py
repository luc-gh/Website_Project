# Código responsável por tornar a pasta 'Website' um Pacote de Python (Python Package)
# Isso será útil ao importar tal pasta para outros códigos, pois todos os objetos daquela serão utilizáveis neles.

# Inicializando a aplicação Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Para o banco de dados
from os import path
from flask_login import LoginManager

db = SQLAlchemy()  # Cria instância do bd
DB_NAME = "database.db"


def criar_app():
    app = Flask(__name__)

    # Configuração que tornará encriptados/protegidos os dados de seção relacionados ao website
    app.config['SECRET_KEY'] = 'ramdom-secret-key'  # A chave é uma string qualquer

    # Definindo onde o database será armazenado e como será usado:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Inicializando db:
    db.init_app(app)
    # Registrando blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Garantindo criação do bd:
    from . import models
    with app.app_context():
        db.create_all()
        # BD criado

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app

