from app.extensions import db_connection as db
from app.models.alumno import Alumno

class AlumnoRepository:
    @staticmethod
    def crear_alumno(nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca):
        sql = """
        INSERT INTO alumnos (nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca)

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
            cursor.close()  # Cerrar el cursor luego de la operación

    @staticmethod
    def obtener_todos_los_alumnos():
        connection = db.get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM alumnos")
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def obtener_alumno_por_id(idalumno):
        connection = db.get_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM alumnos WHERE idalumno = %s", (idalumno,))
            return cursor.fetchone()
        finally:
            cursor.close()

    @staticmethod
    def actualizar_alumno(idalumno, nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca):
        sql = """
        UPDATE alumnos
        SET nombre = %s, apellidos = %s, direccion_postal = %s, direccion_electronica = %s, tiene_beca = %s
        WHERE idalumno = %s
        """
        valores = (nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca, idalumno)

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
    def eliminar_alumno(idalumno):
        connection = db.get_connection()
        if not connection:
            return "Error: No se pudo conectar a la base de datos"

        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM alumnos WHERE idalumno = %s", (idalumno,))
            connection.commit()  # Confirmar eliminación en la base de datos
        except Exception as err:
            connection.rollback()  # Revertir cambios en caso de error
            raise err
        finally:
            cursor.close()
