from flask import session, redirect, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verifica si el usuario está autenticado en la sesión
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))  # Redirige al login si no está autenticado
        return f(*args, **kwargs)
    return decorated_function
