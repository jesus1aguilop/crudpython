from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import User
from app.models import get_database_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_database_connection()
        cursor = db.connection.cursor(dictionary=True)

        try:
            user = User.get_user_by_username(cursor, username)

            if user and User.check_password(user['password'], password):
                session['user_id'] = user['idusuario']
                session['user_name'] = user['username']
                flash('Inicio de sesión exitoso', 'success')
                return redirect(url_for('index'))  # Redirige a la página principal o a donde desees
            else:
                flash('Nombre de usuario o contraseña incorrectos', 'danger')
        except Exception as e:
            flash(f'Ocurrió un error: {str(e)}', 'danger')
        finally:
            cursor.close()
            db.close()

    return render_template('login.html')