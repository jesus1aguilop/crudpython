import flask_session
import os

class Config:
    # Configuración de la base de datos
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_DATABASE = os.environ.get('DB_DATABASE', 'universidad_2')

    # Configuración de sesión
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SECRET_KEY = 'mi-clave-secreta-unica' 