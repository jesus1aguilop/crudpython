import mysql.connector
from flask_session import Session


# Extensión de sesiones
session = Session()

class DBConnection:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'universidad_2'
        }
        self.connection = None

    def get_connection(self):
        if not self.connection or not self.connection.is_connected():
            self.connection = mysql.connector.connect(**self.config)
        return self.connection

db_connection = DBConnection()
