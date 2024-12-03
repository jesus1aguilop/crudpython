from app import db

class Curso(db.Model):
    __tablename__ = 'curso'
    
    idcurso = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero_asignaturas = db.Column(db.Integer, nullable=True)
    
    def __init__(self, nombre, numero_asignaturas):
        self.nombre = nombre
        self.numero_asignaturas = numero_asignaturas

    def __repr__(self):
        return f'<Curso {self.nombre}>'
