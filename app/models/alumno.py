class Alumno:
    def __init__(self, nombre, apellidos, direccion_postal, direccion_electronica=None, tiene_beca=False):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion_postal = direccion_postal
        self.direccion_electronica = direccion_electronica
        self.tiene_beca = tiene_beca

    def __repr__(self):
        return f'<Alumno {self.nombre} {self.apellidos}>'

    # Métodos adicionales que no están relacionados con la base de datos
    def nombre_completo(self):
        return f'{self.nombre} {self.apellidos}'

    # Este es un ejemplo de un método adicional que podría ser útil para el modelo, pero no interactúa con la base de datos.
    def tiene_beca_texto(self):
        return "Sí" if self.tiene_beca else "No"
