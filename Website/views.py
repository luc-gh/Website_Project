# Telas ou endpoints de página funcionais do website (ações de usuário)

# Área de rotas de telas ou interfaces de usuário

from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Aqui será definido que este arquivo possui as rotas de aplicação (blueprint file: URLs definidos)
# Exceção: rotas de autenticação

views = Blueprint('views', __name__)


@views.route('/')  # default page (página inicial)
@login_required
def home():
    return render_template("home.html", user=current_user)
