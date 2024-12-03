from app import db
from app.models import Matricula

class MatriculaRepository:
    
    @staticmethod
    def create_matricula(idalumno, idasignatura):
        try:
            nueva_matricula = Matricula(
                idalumno=idalumno, 
                idasignatura=idasignatura
            )
            db.session.add(nueva_matricula)
            db.session.commit()
            return nueva_matricula
        except Exception as e:
            db.session.rollback()
            print(f"Error al crear matricula: {e}")
            return None
        
    @staticmethod
    def get_all_matriculas():
            try:
                return Matricula.query.all()
            except Exception as e:
                print(f"Error al obtener las matriculas: {e}")
                return []
            
    @staticmethod
    def get_matricula_by_id(idmatricula):
            try:
                return Matricula.query.get(idmatricula)
            except Exception as e:
                print(f"Error al obtener matricula por ID: {e}")
                return None
    
    @staticmethod
    def update_matricula(idmatricula, idalumno, idasignatura):
        try:
            matricula = Matricula.query.get(idmatricula)
            if matricula:
                matricula.idalumno = idalumno
                matricula.idasignatura = idasignatura
                db.session.commit()
                return matricula
            return None
        except Exception as e:
            db.session.rollback()
            print(f"Error al actualizar la matricula: {e}")
            return None
        
    @staticmethod
    def delete_matricula(idmatricula):
        try:
            matricula = Matricula.query.get(idmatricula)
            if matricula:
                db.session.delete(matricula)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar la matricula: {e}")
            return False