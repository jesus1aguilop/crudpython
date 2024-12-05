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
    def get_all_profesores():
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM profesores")
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def get_profesor_by_id(idprofesor):
        cursor = db.cursor(dictionary=True)
        try:
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
    def delete_profesor(idprofesor):
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM profesores WHERE idprofesor = %s", (idprofesor,))
            db.commit()
        except mysql.connector.Error as err:
            db.rollback()
            raise err
        finally:
            cursor.close()
