from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="universidad_2"
)

@app.route('/')
def index():
    return render_template('index.html')  # Carga el archivo HTML con el formulario

# Cambiamos el nombre de la función para evitar el conflicto
@app.route('/formulario')
def formulario():
    return render_template('ingresoAlumno.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Obtener datos del formulario
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')  # Cambiado para coincidir con la columna en la base de datos
    direccion_postal = request.form.get('direccion_postal')
    direccion_electronica = request.form.get('direccion_electronica')
    tiene_beca = request.form.get('tiene_beca') == 'on'  # True si está marcado, False si no

    # Crear cursor para ejecutar comandos SQL
    cursor = db.cursor()

    # Comando SQL para insertar datos en la tabla alumnos
    sql = """
    INSERT INTO alumnos (nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca)
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = (nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca)

    try:
        # Ejecutar el comando SQL e insertar datos
        cursor.execute(sql, valores)
        db.commit()  # Confirmar cambios en la base de datos
        return redirect(url_for('formulario'))
    except mysql.connector.Error as err:
        db.rollback()  # Revertir cambios en caso de error
        return f"Error al guardar los datos: {err}"
    finally:
        cursor.close()  # Cerrar el cursor después de la operación

# Esta es la función que consulta y muestra los registros
@app.route('/reporte')
def reporte():
    try:
        cursor = db.cursor(dictionary=True)  # Usamos un cursor en modo diccionario para facilidad
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()  # Obtener todos los registros
        cursor.close()
        
        # Pasamos los registros de alumnos a la plantilla 'report.html'
        return render_template('report.html', alumnos=alumnos)
    except mysql.connector.Error as err:
        print(f"Error al consultar los datos: {err}")
        return "Error al consultar los datos"


if __name__ == '__main__':
    app.run(debug=True)
