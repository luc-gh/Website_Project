# Autenticação de usuário

from flask import Blueprint, render_template, request, flash

# Aqui serão definidas as rotas de autenticação (URLs) e telas correspondentes

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('firstName')
        password = request.form.get('password1')
        confirm = request.form.get('password2')

        # Verificações sobre os dados passados
        # Para fazer isso, usa-se o recurso de Message Flashing, do Flask
        # Com isso, pode-se fazer verificações e indicar erros de envio ao usuário

        if len(email) < 5:
            flash('O email deve ter mais de 4 caracteres!', category='error')
        elif len(name) < 4:
            flash('O nome deve ter ao menos 4 caracteres!', category='error')
        elif len(password) < 8:
            flash('Sua senha deve ter ao menos 8 dígitos.', category='error')
        elif password != confirm:
            flash('As senhas digitadas não são iguais!', category='error')
        else:
            # Conta válida (aprovada): adicionar nvo usuário ao banco de dados
            flash('Conta criada.', category='success')

        # para mostrar as mensagens de flash, é preciso de um bloco definido no html (base.html)

    return render_template("sign_up.html")