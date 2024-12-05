from app.extensions import db_connection

class Profesor:
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