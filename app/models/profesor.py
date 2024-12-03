from app import db

class Profesor(db.Model):
    __tablename__ = 'profesor'
    
    idprofesor = db.Column(db.Integer, primary_key=True)
    nif = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(100), nullable=True)
    direccion_postal = db.Column(db.String(100), nullable=True)
    direccion_electronica = db.Column(db.String(100), nullable=True)
    categoria = db.Column(db.String(100), nullable=True)

    def __init__(self, nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion_postal = direccion_postal
        self.direccion_electronica = direccion_electronica
        self.categoria = categoria

    def __repr__(self):
        return f'<Profesor {self.nombre} {self.apellidos}>'
