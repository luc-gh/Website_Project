# Telas ou endpoints de página funcionais do website (ações de usuário)

# Área de rotas de telas ou interfaces de usuário

from flask import Blueprint, render_template

# Aqui será definido que este arquivo possui as rotas de aplicação (blueprint file: URLs definidos)
# Exceção: rotas de autenticação

views = Blueprint('views', __name__)


@views.route('/')  # default page (página inicial)
def home():
    return render_template("home.html")
