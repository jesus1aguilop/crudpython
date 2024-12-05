from app.extensions import db_connection

class Matricula:
    def __init__(self, idalumno, idasignatura):
        self.idalumno = idalumno
        self.idasignatura = idasignatura
    
    def __repr__(self):
        return f'<Matricula {self.idalumno} {self.idasignatura}>'