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
        cursor = db.cursor()
        try:
            cursor.execute(sql, valores)
            db.commit()
        except Exception as err:
            db.rollback()
            raise err
        finally:
            cursor.close()

    @staticmethod
    def obtener_todos_los_alumnos():
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM alumnos")
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def obtener_alumno_por_id(idalumno):
        cursor = db.cursor(dictionary=True)
        try:
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
        cursor = db.cursor()
        try:
            cursor.execute(sql, valores)
            db.commit()
        except Exception as err:
            db.rollback()
            raise err
        finally:
            cursor.close()

    @staticmethod
    def eliminar_alumno(idalumno):
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM alumnos WHERE idalumno = %s", (idalumno,))
            db.commit()
        except Exception as err:
            db.rollback()
            raise err
        finally:
            cursor.close()
