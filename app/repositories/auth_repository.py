import mysql.connector
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

class AuthRepository:
    @staticmethod
    def get_user_by_username(username):
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            cursor.close()
            return user
        except mysql.connector.Error as err:
            print(f"Error al consultar el usuario: {err}")
            return None

    @staticmethod
    def create_user(username, password):
        try:
            cursor = db.cursor()
            hashed_password = generate_password_hash(password)

            # Verificar si el usuario ya existe
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                cursor.close()
                return None

            # Insertar el nuevo usuario
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            db.commit()
            cursor.close()

            return True
        except mysql.connector.Error as err:
            print(f"Error al registrar el usuario: {err}")
            return False
