from app import db

class Asignatura(db.Model):
    __tablename__ = 'asignaturas'
    
    idasignatura = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    creditos = db.Column(db.Integer, nullable=True)
    cuatrimestre = db.Column(db.Integer, nullable=True)
    caracter = db.Column(db.String(1), nullable=True)
    
    def __init__(self, nombre, creditos, cuatrimestre, caracter):
        self.nombre = nombre
        self.creditos = creditos
        self.cuatrimestre = cuatrimestre
        self.caracter = caracter

    def __repr__(self):
        return f'<Asignatura {self.nombre}>'
