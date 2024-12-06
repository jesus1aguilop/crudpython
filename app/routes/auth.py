from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.repositories.auth_repository import AuthRepository

auth_bp = Blueprint('auth', __name__, template_folder='../templates/auth')

@auth_bp.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))  # Cambiado aquí
    return render_template('index.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = AuthRepository.get_by_username(username)

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.idusuario
            session['user_name'] = user.username
            print('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('auth.index'))  # Cambiado aquí
        else:
            print('Usuario o contraseña incorrectos.', 'danger')
            return redirect(url_for('auth.login'))  # Cambiado aquí

    return render_template('login.html')


@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if AuthRepository.user_exists(username):
            print('El usuario ya existe.', 'danger')
            return redirect(url_for('auth.registro'))  # Cambiado aquí

        hashed_password = generate_password_hash(password)
        AuthRepository.create_user(username, hashed_password)
        print('Usuario registrado exitosamente.', 'success')
        return redirect(url_for('auth.login'))  # Cambiado aquí

    return render_template('registro.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    print('Sesión cerrada exitosamente.', 'success')
    return redirect(url_for('auth.login'))  # Cambiado aquí
