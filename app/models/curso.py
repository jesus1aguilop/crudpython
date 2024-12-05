class Curso:
    def __init__(self, nombre, numero_asignaturas):
        self.nombre = nombre
        self.numero_asignaturas = numero_asignaturas

    def __repr__(self):
        return f"Curso {self.nombre}, {self.numero_asignaturas}"

    # Métodos adicionales que no están relacionados con la base de datos
    def descripcion(self):
        return f"{self.nombre} tiene {self.numero_asignaturas} asignaturas."
