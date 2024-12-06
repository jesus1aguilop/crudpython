import os
import mysql.connector
from flask_session import Session
import mysql.connector

# Extensión de sesiones
session = Session()

class DBConnection:
    def __init__(self):
        self.config = {
            'host': os.environ.get('DB_HOST', 'localhost'),
            'user': os.environ.get('DB_USER', 'root'),
            'password': os.environ.get('DB_PASSWORD', ''),
            'database': os.environ.get('DB_DATABASE', 'universidad_2')
        }
        self.connection = None
        
    def get_connection(self):
        try:
            if not self.connection or not self.connection.is_connected():
                self.connection = mysql.connector.connect(**self.config)
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def __enter__(self):
        return self.get_connection()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

db_connection = DBConnection()
