# Autenticação de usuário

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# Aqui serão definidas as rotas de autenticação (URLs) e telas correspondentes

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login feito com sucesso!', category='success')

                login_user(user, remember=True)  # Reconhece usuário ativo

                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta!', category='error')
        else:
            flash('Esse email não existe!', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('firstName')
        password = request.form.get('password1')
        confirm = request.form.get('password2')

        # Para ver se o email já existe:
        user = User.query.filter_by(email=email).first()

        # Verificações sobre os dados passados
        # Para fazer isso, usa-se o recurso de Message Flashing, do Flask
        # Com isso, pode-se fazer verificações e indicar erros de envio ao usuário
        if user:
            flash('O email já existe!', category='error')
        elif len(email) < 5:
            flash('O email deve ter mais de 4 caracteres!', category='error')
        elif len(name) < 4:
            flash('O nome deve ter ao menos 4 caracteres!', category='error')
        elif len(password) < 8:
            flash('Sua senha deve ter ao menos 8 dígitos.', category='error')
        elif password != confirm:
            flash('As senhas digitadas não são iguais!', category='error')
        else:
            # Conta válida (aprovada): adicionar novo usuário ao banco de dados
            new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(user, remember=True)  # Reconhece usuário ativo

            flash('Conta criada.', category='success')

            # Redirecionando para página principal
            return redirect(url_for('views.home'))

        # para mostrar as mensagens de flash, é preciso de um bloco definido no html (base.html)

    return render_template("sign_up.html", user=current_user)