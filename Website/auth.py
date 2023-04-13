# Autenticação de usuário

from flask import Blueprint, render_template

# Aqui serão definidas as rotas de autenticação (URLs) e telas correspondentes

auth = Blueprint('auth', __name__)

# Lidando com requisições do tipo POST


@auth.route('/login', methods=['GET', 'POST'])  # Métodos que serão interpretados para requisições
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")