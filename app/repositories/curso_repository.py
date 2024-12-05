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
            def get_all_cursos():
                cursor = db.cursor(dictionary=True)
                try:
                    cursor.execute("SELECT * FROM cursos")
                    return cursor.fetchall()
                finally:
                    cursor.close()
                
            @staticmethod
            def get_curso_by_id(idcurso):
                cursor = db.cursor(dictionary=True)
                try:
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
            cursor = db.cursor()

            try:
                cursor.execute(sql, valores)
                db.commit()
            except mysql.connector.Error as err:
                db.rollback()
                raise err
            finally:
                cursor.close()

        @staticmethod
        def delete_curso(idcurso):
            cursor = db.cursor()
            try:
                cursor.execute("DELETE FROM cursos WHERE idcurso = %s", (idcurso,))
                db.commit()
            except mysql.connector.Error as err:
                db.rollback()
                raise err
            finally:
                cursor.close()