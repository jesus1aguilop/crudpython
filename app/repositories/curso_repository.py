from app.extensions import db_connection as db
import mysql.connector

class CursoRepository:
    @staticmethod
    def create_curso(nombre, numero_asignaturas):
        sql = """
        INSERT INTO cursos (nombre, numero_asignaturas)
        VALUES (%s, %s)
        """
        valores = (nombre, numero_asignaturas)
        
        connection = db.get_connection()  # Obtener la conexión
        if not connection:
            return "Error: No se pudo conectar a la base de datos"

        try:
            cursor = connection.cursor()
            cursor.execute(sql, valores)
            connection.commit()  # Confirmar cambios en la base de datos
            return True
        except mysql.connector.Error as err:
            connection.rollback()  # Revertir cambios en caso de error
            return f"Error al guardar los datos: {err}"
        finally:
            cursor.close()  # Cerrar el cursor luego de la operación

    @staticmethod
    def get_all_cursos():
        connection = db.get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM cursos")
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def get_curso_by_id(idcurso):
        connection = db.get_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM cursos WHERE idcurso = %s", (idcurso,))
            return cursor.fetchone()
        finally:
            cursor.close()

    @staticmethod
    def update_curso(idcurso, nombre, numero_asignaturas):
        sql = """
        UPDATE cursos
        SET nombre = %s, numero_asignaturas = %s
        WHERE idcurso = %s
        """
        valores = (nombre, numero_asignaturas, idcurso)
        
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
            return f"Error al actualizar los datos: {err}"
        finally:
            cursor.close()

    @staticmethod
    def delete_curso(idcurso):
        connection = db.get_connection()
        if not connection:
            return "Error: No se pudo conectar a la base de datos"

        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM cursos WHERE idcurso = %s", (idcurso,))
            connection.commit()
            return True
        except mysql.connector.Error as err:
            connection.rollback()
            return f"Error al eliminar los datos: {err}"
        finally:
            cursor.close()
