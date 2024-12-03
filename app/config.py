import os

class Config:
    # Configuración de la base de datos
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_DATABASE = os.environ.get('DB_DATABASE', 'universidad_2')

    # Otras configuraciones
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')