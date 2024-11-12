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

# endpoint del formulario de Alumno
@app.route('/formulario')
def formulario():
    return render_template('ingresoAlumno.html')

#funcion que recibe los datos del formulario de Alumno
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Obtener datos del formulario
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')  
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
        
        # Pasamos los registros de alumnos a la plantilla 'reportAlumno.html'
        return render_template('reportAlumno.html', alumnos=alumnos)
    except mysql.connector.Error as err:
        print(f"Error al consultar los datos: {err}")
        return "Error al consultar los datos"

# endpoint del formulario de Profesor
@app.route('/formulario1')
def formulario1():
    return render_template('IngresoProfesor.html')

#funcion que recibe los datos del formulario de Profesor
@app.route('/submit_form1', methods=['POST'])
def submit_form1():
    nif = request.form.get('nif')
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    telefono = request.form.get('telefono')
    direccion_postal = request.form.get('direccion_postal')   
    direccion_electronica = request.form.get('direccion_electronica')
    categoria = request.form.get('categoria')

    # Crear cursor para ejecutar comandos SQL
    cursor = db.cursor()
    # Comando SQL para insertar datos en la tabla profesores
    sql = """
    INSERT INTO profesor (nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria)

    try:
        # Ejecutar el comando SQL e insertar datos
        cursor.execute(sql, valores)
        db.commit()  # Confirmar cambios en la base de datos
        return redirect(url_for('formulario1'))
    except mysql.connector.Error as err:
        db.rollback()  # Revertir cambios en caso de error
        return f"Error al guardar los datos: {err}"
    finally:
        cursor.close()  # Cerrar el cursor luego de la operación

# Esta es la función que consulta y muestra los registros para el reporte de profesores
@app.route('/reporteProfesor')
def reporteProfesor():
    try:
        cursor = db.cursor(dictionary=True)  # Usamos un cursor en modo diccionario para facilidad
        cursor.execute("SELECT * FROM profesor")  # Cambiado a la tabla 'profesor'
        profesores = cursor.fetchall()  # Obtener todos los registros de profesores
        cursor.close()
        
        # Pasamos los registros de profesores a la plantilla 'reportProfesor.html'
        return render_template('reportProfesor.html', profesores=profesores)
    except mysql.connector.Error as err:
        print(f"Error al consultar los datos: {err}")
        return "Error al consultar los datos"

@app.route('/formulario2')
def formulario2():
    return render_template('IngresoCurso.html')

@app.route('/submit_form2', methods=['POST'])
def submit_form2():
    nombre = request.form.get('nombre')
    numero_asignaturas = request.form.get('numero_asignaturas')

    # Crear cursor para ejecutar comandos SQL
    cursor = db.cursor()

    # Comando SQL para insertar datos en la tabla curso
    sql = """
    INSERT INTO curso (nombre, numero_asignaturas)
    VALUES (%s, %s)
    """
    valores = (nombre, numero_asignaturas)

    try:
        # Ejecutar el comando SQL e insertar datos
        cursor.execute(sql, valores)
        db.commit()  # Confirmar cambios en la base de datos
        return redirect(url_for('formulario2'))
    except mysql.connector.Error as err:
        db.rollback()  # Revertir cambios en caso de error
        return f"Error al guardar los datos: {err}"
    finally:
        cursor.close()  # Cerrar el cursor después de la operación

@app.route('/reporteCurso')
def reporteCurso():
    try:
        cursor = db.cursor(dictionary=True)  # Usamos un cursor en modo diccionario para facilidad
        cursor.execute("SELECT * FROM curso")  # Cambiado a la tabla 'profesor'
        profesores = cursor.fetchall()  # Obtener todos los registros de profesores
        cursor.close()
        
        # Pasamos los registros de profesores a la plantilla 'reportProfesor.html'
        return render_template('reporteCurso.html', profesores=profesores)
    except mysql.connector.Error as err:
        print(f"Error al consultar los datos: {err}")
        return "Error al consultar los datos"

if __name__ == '__main__':
    app.run(debug=True)
