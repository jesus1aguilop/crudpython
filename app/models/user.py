# app/models/user.py
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    @staticmethod
    def create_user(cursor, username, password):
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, generate_password_hash(password)))

    @staticmethod
    def get_user_by_username(cursor, username):
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        return cursor.fetchone()

    @staticmethod
    def check_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)