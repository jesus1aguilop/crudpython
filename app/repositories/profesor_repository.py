from app import db
from app.models import Profesor

class ProfesorRepository:

    @staticmethod
    def create_profesor(nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria):
        try:
            nuevo_profesor = Profesor(
                nif=nif,
                nombre=nombre,
                apellidos=apellidos,
                telefono=telefono,
                direccion_postal=direccion_postal,
                direccion_electronica=direccion_electronica,
                categoria=categoria
            )
            db.session.add(nuevo_profesor)
            db.session.commit()
            return nuevo_profesor
        except Exception as e:
            db.session.rollback()
            print(f"Error al crear profesor: {e}")
            return None

    @staticmethod
    def get_all_profesores():
        try:
            return Profesor.query.all()
        except Exception as e:
            print(f"Error al obtener los profesores: {e}")
            return []

    @staticmethod
    def get_profesor_by_id(idprofesor):
        try:
            return Profesor.query.get(idprofesor)
        except Exception as e:
            print(f"Error al obtener profesor por ID: {e}")
            return None

    @staticmethod
    def update_profesor(idprofesor, nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria):
        try:
            profesor = Profesor.query.get(idprofesor)
            if profesor:
                profesor.nif = nif
                profesor.nombre = nombre
                profesor.apellidos = apellidos
                profesor.telefono = telefono
                profesor.direccion_postal = direccion_postal
                profesor.direccion_electronica = direccion_electronica
                profesor.categoria = categoria
                db.session.commit()
                return profesor
            return None
        except Exception as e:
            db.session.rollback()
            print(f"Error al actualizar el profesor: {e}")
            return None

    @staticmethod
    def delete_profesor(idprofesor):
        try:
            profesor = Profesor.query.get(idprofesor)
            if profesor:
                db.session.delete(profesor)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar el profesor: {e}")
            return False
