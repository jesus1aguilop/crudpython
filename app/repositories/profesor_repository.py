from app.extensions import db_connection as db
import mysql.connector


class ProfesorRepository:

    @staticmethod
    def create_profesor(nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria):
        sql = """
        INSERT INTO profesor (nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria)
        
        connection = db.get_connection()  # Obtener la conexión
        if not connection:
            return "Error: No se pudo conectar a la base de datos"
        
        try:
            cursor = connection.cursor()
            cursor.execute(sql, valores)
            connection.commit()
            return True
        except mysql.connector.Error as err:
            connection.rollback()
            return f"Error al guardar los datos: {err}"
        finally:
            cursor.close()

    @staticmethod
    def get_all_profesores():
        connection = db.get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM profesores")
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def get_profesor_by_id(idprofesor):
        connection = db.get_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM profesores WHERE idprofesor = %s", (idprofesor,))
            return cursor.fetchone()
        finally:
            cursor.close()

    @staticmethod
    def update_profesor(idprofesor, nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria):
        sql = """
        UPDATE profesores
        SET nif = %s, nombre = %s, apellidos = %s, telefono = %s, direccion_postal = %s, direccion_electronica = %s, categoria = %s
        WHERE idprofesor = %s
        """
        valores = (nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria, idprofesor)

        connection = db.get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            cursor.execute(sql, valores)
            connection.commit()
            return True
        except mysql.connector.Error as err:
            connection.rollback()
            raise err
        finally:
            cursor.close()

    @staticmethod
    def delete_profesor(idprofesor):
        connection = db.get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM profesores WHERE idprofesor = %s", (idprofesor,))
            connection.commit()
            return True
        except mysql.connector.Error as err:
            connection.rollback()
            raise err
        finally:
            cursor.close()
