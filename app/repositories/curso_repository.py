from app import db
from app.models import Curso

class CursoRepository:

    @staticmethod
    def create_curso(nombre, numero_asignaturas):
        try:
            nuevo_curso = Curso(
                nombre=nombre,
                numero_asignaturas=numero_asignaturas
            )
            db.session.add(nuevo_curso)
            db.session.commit()
            return nuevo_curso
        except Exception as e:
            db.session.rollback()
            print(f"Error al crear curso: {e}")
            return None

    @staticmethod
    def get_all_cursos():
        try:
            return Curso.query.all()
        except Exception as e:
            print(f"Error al obtener los cursos: {e}")
            return []

    @staticmethod
    def get_curso_by_id(idcurso):
        try:
            return Curso.query.get(idcurso)
        except Exception as e:
            print(f"Error al obtener curso por ID: {e}")
            return None

    @staticmethod
    def update_curso(idcurso, nombre, numero_asignaturas):
        try:
            curso = Curso.query.get(idcurso)
            if curso:
                curso.nombre = nombre
                curso.numero_asignaturas = numero_asignaturas
                db.session.commit()
                return curso
            return None
        except Exception as e:
            db.session.rollback()
            print(f"Error al actualizar el curso: {e}")
            return None

    @staticmethod
    def delete_curso(idcurso):
        try:
            curso = Curso.query.get(idcurso)
            if curso:
                db.session.delete(curso)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar el curso: {e}")
            return False
