from app import db

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    
    idalumno = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    direccion_postal = db.Column(db.String(100), unique=True, nullable=False)
    direccion_electronica = db.Column(db.String(100), nullable=True)
    tiene_beca = db.Column(db.Boolean, nullable=False, default=False)
    
    def __init__(self, nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca=False):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion_postal = direccion_postal
        self.direccion_electronica = direccion_electronica
        self.tiene_beca = tiene_beca

    def __repr__(self):
        return f'<Alumno {self.nombre} {self.apellidos}>'
