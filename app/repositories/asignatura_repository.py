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
        cursor = db.cursor()
        try:
            cursor.execute(sql, valores)
            db.commit()
            return cursor.lastrowid
        except Exception as err:
            db.rollback()
            raise err
        finally:
            cursor.close()

    @staticmethod
    def get_all_asignaturas():
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM asignatura")
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def get_asignatura_by_id(idasignatura):
        cursor = db.cursor(dictionary=True)
        try:
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
    def delete_asignatura(idasignatura):
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM asignatura WHERE idasignatura = %s", (idasignatura,))
            db.commit()
        except Exception as err:
            db.rollback()
            raise err
        finally:
            cursor.close()