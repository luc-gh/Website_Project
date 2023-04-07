# Autenticação de usuário

from flask import Blueprint

# Aqui serão definidas as rotas de autenticação (URLs) e telas correspondentes

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>Login</p>"  # Esse tipo de retorno foi usado aqui apenas para verificar se as rotas estão funcionando


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"  # Tais retorno serão removidos nos próximos commits


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"  # E serão adicionadas interfaces com Jinja2, na pasta templates