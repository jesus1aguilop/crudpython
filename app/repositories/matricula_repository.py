from app.extensions import db_connection as db
import mysql.connector

class MatriculaRepository:

    @staticmethod
    def create_matricula(idalumno, idasignatura):
        sql = """
        INSERT INTO matricula (idalumno, idasignatura)
        VALUES (%s, %s)
        """
        valores = (idalumno, idasignatura)

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
    def get_all_alumnos():
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
    def get_all_matriculas():
        connection = db.get_connection()
        if not connection:
            return []

        try:
            cursor = connection.cursor(dictionary=True)
            # Hacer un JOIN entre las tablas matricula, alumnos y asignatura
            cursor.execute("""
                SELECT 
                    m.idmatricula,
                    a.nombre AS alumno_nombre,
                    a.apellidos AS alumno_apellidos,
                    s.nombre AS asignatura_nombre
                FROM matricula m
                JOIN alumnos a ON m.idalumno = a.idalumno
                JOIN asignatura s ON m.idasignatura = s.idasignatura
            """)
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def get_matricula_by_id(idalumno, idasignatura):
        connection = db.get_connection()
        if not connection:
            return None

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM matricula WHERE idalumno = %s AND idasignatura = %s", (idalumno, idasignatura))
            return cursor.fetchone()
        finally:
            cursor.close()

    @staticmethod
    def delete_matricula(idalumno, idasignatura):
        connection = db.get_connection()
        if not connection:
            return False

        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM matricula WHERE idalumno = %s AND idasignatura = %s", (idalumno, idasignatura))
            connection.commit()
            return True
        except Exception as err:
            connection.rollback()
            return f"Error al eliminar los datos: {err}"
        finally:
            cursor.close()

    @staticmethod
    def update_matricula(idalumno, idasignatura):
        connection = db.get_connection()
        if not connection:
            return False

        sql = """
        UPDATE matricula 
        SET idalumno = %s, idasignatura = %s 
        WHERE idalumno = %s AND idasignatura = %s
        """
        valores = (idalumno, idasignatura, idalumno, idasignatura)

        try:
            cursor = connection.cursor()
            cursor.execute(sql, valores)
            connection.commit()
            return True
        except Exception as err:
            connection.rollback()
            return f"Error al actualizar los datos: {err}"
        finally:
            cursor.close()
