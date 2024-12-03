from app import db
from app.models import Asignatura

class AsignaturaRepository:

    @staticmethod
    def create_asignatura(nombre, creditos, cuatrimestre, caracter):
        try:
            nueva_asignatura = Asignatura(
                nombre=nombre,
                creditos=creditos,
                cuatrimestre=cuatrimestre,
                caracter=caracter
            )
            db.session.add(nueva_asignatura)
            db.session.commit()
            return nueva_asignatura
        except Exception as e:
            db.session.rollback()
            print(f"Error al crear asignatura: {e}")
            return None

    @staticmethod
    def get_all_asignaturas():
        try:
            return Asignatura.query.all()
        except Exception as e:
            print(f"Error al obtener las asignaturas: {e}")
            return []

    @staticmethod
    def get_asignatura_by_id(idasignatura):
        try:
            return Asignatura.query.get(idasignatura)
        except Exception as e:
            print(f"Error al obtener asignatura por ID: {e}")
            return None

    @staticmethod
    def update_asignatura(idasignatura, nombre, creditos, cuatrimestre, caracter):
        try:
            asignatura = Asignatura.query.get(idasignatura)
            if asignatura:
                asignatura.nombre = nombre
                asignatura.creditos = creditos
                asignatura.cuatrimestre = cuatrimestre
                asignatura.caracter = caracter
                db.session.commit()
                return asignatura
            return None
        except Exception as e:
            db.session.rollback()
            print(f"Error al actualizar la asignatura: {e}")
            return None

    @staticmethod
    def delete_asignatura(idasignatura):
        try:
            asignatura = Asignatura.query.get(idasignatura)
            if asignatura:
                db.session.delete(asignatura)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar la asignatura: {e}")
            return False
