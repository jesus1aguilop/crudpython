from app.extensions import db_connection as db
from app.models.asignatura import Asignatura

class AsignaturaRepository:
    @staticmethod
    def create_asignatura(nombre, creditos, cuatrimestre, caracter):
        sql = """
        INSERT INTO asignatura (nombre, creditos, cuatrimestre, caracter)
        VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, creditos, cuatrimestre, caracter)
        
        connection = db.get_connection()  # Obtener la conexión
        if not connection:
            return "Error: No se pudo conectar a la base de datos"

        try:
            cursor = connection.cursor()
            cursor.execute(sql, valores)
            connection.commit()  # Confirmar cambios en la base de datos
            return cursor.lastrowid
        except Exception as err:
            connection.rollback()  # Revertir cambios en caso de error
            raise err
        finally:
            cursor.close()  # Cerrar el cursor luego de la operación

    @staticmethod
    def get_all_asignaturas():
        connection = db.get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM asignatura")
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def get_asignatura_by_id(idasignatura):
        connection = db.get_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM asignatura WHERE idasignatura = %s", (idasignatura,))
            return cursor.fetchone()
        finally:
            cursor.close()

    @staticmethod
    def update_asignatura(idasignatura, nombre, creditos, cuatrimestre, caracter):
        sql = """
        UPDATE asignatura
        SET nombre = %s, creditos = %s, cuatrimestre = %s, caracter = %s
        WHERE idasignatura = %s
        """
        valores = (nombre, creditos, cuatrimestre, caracter, idasignatura)
        
        connection = db.get_connection()  # Obtener la conexión
        if not connection:
            return "Error: No se pudo conectar a la base de datos"

        try:
            cursor = connection.cursor()
            cursor.execute(sql, valores)
            connection.commit()  # Confirmar cambios en la base de datos
        except Exception as err:
            connection.rollback()  # Revertir cambios en caso de error
            raise err
        finally:
            cursor.close()

    @staticmethod
    def delete_asignatura(idasignatura):
        connection = db.get_connection()
        if not connection:
            return "Error: No se pudo conectar a la base de datos"

        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM asignatura WHERE idasignatura = %s", (idasignatura,))
            connection.commit()  # Confirmar eliminación en la base de datos
        except Exception as err:
            connection.rollback()  # Revertir cambios en caso de error
            raise err
        finally:
            cursor.close()
