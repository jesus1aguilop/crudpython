from app.extensions import db_connection
from app.models.auth import Auth 

class AuthRepository:
    @staticmethod
    def get_by_username(username):
        """Obtiene un usuario por su username."""
        connection = db_connection.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        cursor.close()
        return Auth.from_dict(user_data) if user_data else None

    @staticmethod
    def create_user(username, hashed_password):
        """Crea un nuevo usuario en la base de datos."""
        connection = db_connection.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, hashed_password),
        )
        connection.commit()
        cursor.close()

    @staticmethod
    def user_exists(username):
        """Verifica si un usuario ya existe en la base de datos."""
        connection = db_connection.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        exists = cursor.fetchone() is not None
        cursor.close()
        return exists
