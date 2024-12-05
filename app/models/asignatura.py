
class Asignatura:
    def __init__(self, idasignatura, nombre):
        self.idasignatura = idasignatura
        self.nombre = nombre

    def __repr__(self):
        return f'<Asignatura {self.nombre}>'

    # Métodos adicionales que no están relacionados con la base de datos
    def nombre_upper(self):
        return self.nombre.upper()
