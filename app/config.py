import flask_session
import os

class Config:
    # Configuración de la base de datos
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_DATABASE = os.environ.get('DB_DATABASE', 'universidad_2')

    # Otras configuraciones
    SESSION_TYPE = 'filesystem'  # Almacena sesiones en el sistema de archivos
    SESSION_PERMANENT = False  # No hace que las sesiones sean permanentes
    SECRET_KEY = 'your_secret_key' # Clave para firmar las cookies y las sesionesandom(24)  # Clave para firmar las sesiones
    
    