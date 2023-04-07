# Telas ou endpoints de página funcionais do website (ações de usuário)

# Área de rotas de telas ou interfaces de usuário

from flask import Blueprint

# Aqui será definido que este arquivo possui as rotas de aplicação (blueprint file: URLs definidos)
# Exceção: rotas de autenticação

views = Blueprint('views', __name__)


@views.route('/')  # default page (página inicial)
def home():
    return "<h1>views.route home test</h1>"
