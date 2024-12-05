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
        cursor = db.cursor()

        try:
            # Ejecutar el comando SQL e insertar datos
            cursor.execute(sql, valores)
            db.commit()  # Confirmar cambios en la base de datos
        except mysql.connector.Error as err:
            db.rollback()  # Revertir cambios en caso de error
            return f"Error al guardar los datos: {err}"
        finally:
            cursor.close()  # Cerrar el cursor luego de la operación
            
    @staticmethod
    def get_all_alumnos():
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM alumnos")
            return cursor.fetchall()
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
    def get_all_matriculas():
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM matricula")
            return cursor.fetchall()
        finally:
            cursor.close()
            
    @staticmethod
    def get_matricula_by_id(idalumno, idasignatura):
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM matricula WHERE idalumno = %s AND idasignatura = %s", (idalumno, idasignatura))
            return cursor.fetchone()
        finally:
            cursor.close()
            
    @staticmethod
    def delete_matricula(idalumno, idasignatura):
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM matricula WHERE idalumno = %s AND idasignatura = %s", (idalumno, idasignatura))
            db.commit()
        except Exception as err:
            db.rollback()
            return f"Error al guardar los datos: {err}"
        finally:
            cursor.close()
            
    @staticmethod
    def update_matricula(idalumno, idasignatura):
        cursor = db.cursor()
        try:
            cursor.execute("UPDATE matricula SET idalumno = %s, idasignatura = %s WHERE idalumno = %s AND idasignatura = %s", (idalumno, idasignatura, idalumno, idasignatura))
            db.commit()
        except Exception as err:
            db.rollback()
            return f"Error al guardar los datos: {err}"
        finally:
            cursor.close()