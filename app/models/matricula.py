from app import db

class Matricula(db.Model):
    
    __tablename__ = 'matricula'
    
    idmatricula = db.Column(db.Integer, primary_key=True)
    idalumno = db.Column(db.Integer, db.ForeignKey('alumnos.idalumno'), nullable=False)
    idasignatura = db.Column(db.Integer, db.ForeignKey('asignaturas.idasignatura'), nullable=False)
    def __init__(self, idalumno, idasignatura, idcurso):
        self.idalumno = idalumno
        self.idasignatura = idasignatura


    def __repr__(self):
        return f'<Matricula {self.idalumno} {self.idasignatura}>'

    #def to_dict(self):
    #    return {
    #        'idmatricula': self.idmatricula,
    #        'idalumno': self.idalumno,
    #        'idasignatura': self.idasignatura,
    #        'idcurso': self.idcurso
    #    }s