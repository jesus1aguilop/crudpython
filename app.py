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

# Mostrar formulario de edición de alumno
@app.route('/editar_alumno/<int:idalumno>', methods=['GET', 'POST'])
def editar_alumno(idalumno):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        direccion_postal = request.form.get('direccion_postal')
        direccion_electronica = request.form.get('direccion_electronica')
        tiene_beca = request.form.get('tiene_beca') == 'on'

        # Actualizar datos en la base de datos
        sql = """
        UPDATE alumnos
        SET nombre = %s, apellidos = %s, direccion_postal = %s, direccion_electronica = %s, tiene_beca = %s
        WHERE idalumno = %s
        """
        valores = (nombre, apellidos, direccion_postal, direccion_electronica, tiene_beca, idalumno)
        
        try:
            cursor.execute(sql, valores)
            db.commit()
            return redirect(url_for('reporte'))
        except mysql.connector.Error as err:
            db.rollback()
            return f"Error al actualizar el alumno: {err}"
        finally:
            cursor.close()  # Asegúrate de cerrar el cursor aquí

    else:
        # Obtener datos del alumno para mostrarlos en el formulario
        cursor.execute("SELECT * FROM alumnos WHERE idalumno = %s", (idalumno,))
        alumno = cursor.fetchone()
        cursor.close()
        
        if alumno is None:
            print('Alumno no encontrado', 'error')
            return redirect(url_for('reporte'))  # Redirigir si el alumno no existe
        
        return render_template('editarAlumno.html', alumno=alumno)


# Función para eliminar un alumno
@app.route('/eliminar_alumno/<int:idalumno>', methods=['POST'])
def eliminar_alumno(idalumno):
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM alumnos WHERE idalumno = %s", (idalumno,))
        db.commit()
        return redirect(url_for('reporte'))
    except mysql.connector.Error as err:
        db.rollback()
        return f"Error al eliminar el alumno: {err}"
    finally:
        cursor.close()  # Siempre cierra el cursor aquí también
        
# endpoint del formulario de Profesor
@app.route('/formulario1')
def formulario1():
    return render_template('IngresoProfesor.html')

# Función que recibe los datos del formulario de Profesor
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
    # Comando SQL para insertar datos en la tabla 'profesor'
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
        
        # Pasamos los registros de profesores a la plantilla 'reporteProfesor.html'
        return render_template('reporteProfesor.html', profesores=profesores)
    except mysql.connector.Error as err:
        print(f"Error al consultar los datos: {err}")
        return "Error al consultar los datos"

@app.route('/eliminar_profesor/<int:idprofesor>', methods=["POST"])
def eliminar_profesor(idprofesor):
    try: 
        cursor = db.cursor()
        cursor.execute("DELETE FROM profesor WHERE idprofesor = %s", (idprofesor,))  # Cambiado a la tabla 'profesor'
        db.commit()
        return redirect(url_for('reporteProfesor'))  # Corregido la ruta de redirección
    except mysql.connector.Error as err:
        db.rollback()
        return f"Error al eliminar el profesor: {err}"
    finally:
        cursor.close()

# Función para editar profesor
@app.route('/editar_profesor/<int:idprofesor>', methods=['GET', 'POST'])
def editar_profesor(idprofesor):
    if request.method == 'POST':
        nif = request.form.get('nif')
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        telefono = request.form.get('telefono')
        direccion_postal = request.form.get('direccion_postal')   
        direccion_electronica = request.form.get('direccion_electronica')
        categoria = request.form.get('categoria')
        
        try:
            cursor = db.cursor()
            cursor.execute("""
                UPDATE profesor
                SET nif = %s, nombre = %s, apellidos = %s, telefono = %s, direccion_postal = %s, direccion_electronica = %s, categoria = %s
                WHERE idprofesor = %s
            """, (nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria, idprofesor))
            
            db.commit()
            print("Profesor actualizado con éxito", "success")
            return redirect(url_for('reporteProfesor'))
        
        except mysql.connector.Error as err: 
            db.rollback()
            print(f"Error al editar el profesor: {err}", "error")
            return redirect(url_for('editar_profesor', idprofesor=idprofesor))
        
        finally:
            cursor.close()
    
    else:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM profesor WHERE idprofesor = %s", (idprofesor,))  # Cambiado a la tabla 'profesor'
        profesor = cursor.fetchone()
        cursor.close()
        
        if profesor is None:
            print("Profesor no encontrado", "error")
            return redirect(url_for('reporteProfesor'))
        
        return render_template('editarProfesor.html', profesor=profesor)
    
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
        cursos = cursor.fetchall()  # Obtener todos los registros de profesores
        cursor.close()
        
        # Pasamos los registros de profesores a la plantilla 
        return render_template('reportCurso.html', cursos=cursos)
    except mysql.connector.Error as err:
        print(f"Error al consultar los datos: {err}")
        return "Error al consultar los datos"
    
# Endpoint de eliminación de curso
@app.route('/eliminar_curso/<int:idcurso>', methods=["POST"])
def eliminar_curso(idcurso):
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM cursos WHERE idcurso = %s", (idcurso,))  # Corregir el paso de la tupla
        db.commit()
        return redirect(url_for('reporteCurso'))
    except mysql.connector.Error as err:
        db.rollback()
        return f"Error al eliminar el curso: {err}"
    finally:
        cursor.close()

# Función de edición de curso
@app.route('/editar_curso/<int:idcurso>', methods=['GET', 'POST'])
def editar_curso(idcurso):
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        numero_asignaturas = request.form.get('numero_asignaturas')
    
        try:
            cursor = db.cursor()
            cursor.execute("""
                UPDATE cursos
                SET nombre = %s, numero_asignaturas = %s  # Corregir el nombre de la columna
                WHERE idcurso = %s
            """, (nombre, numero_asignaturas, idcurso))
            db.commit()
            return redirect(url_for('reporteCurso'))
        except mysql.connector.Error as err:
            db.rollback()
            return f"Error al editar el curso: {err}"
        finally:
            cursor.close()
    else:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cursos WHERE idcurso = %s", (idcurso,))
        curso = cursor.fetchone()  # Cambié aquí 'curso' por 'cursor'
        cursor.close()
        
        if curso is None:
            print('Curso no encontrado', 'error')
            return redirect(url_for('reporteCurso'))  # Redirigir si el curso no existe
        
        return render_template('editarCurso.html', curso=curso)

@app.route('/formulario3')
def formulario3():
    return render_template('IngresoAsignatura.html')
    

@app.route('/submit_form3', methods=['POST'])
def submit_form3():
    nombre = request.form.get('nombre')
    creditos = request.form.get('creditos')
    cuatrimestre = request.form.get('cuatrimestre')
    caracter = request.form.get('caracter')

    # Crear cursor para ejecutar comandos SQL
    cursor = db.cursor()

    # Comando SQL para insertar datos en la tabla asignatura
    sql = """
    INSERT INTO asignatura (nombre, creditos, cuatrimestre, caracter)
    VALUES (%s, %s, %s, %s)
    """
    valores = (nombre, creditos, cuatrimestre, caracter)

    try:
        # Ejecutar el comando SQL e insertar datos
        cursor.execute(sql, valores)
        db.commit()  # Confirmar cambios en la base de datos
        return redirect(url_for('formulario3'))
    except mysql.connector.Error as err:
        db.rollback()  # Revertir cambios en caso de error
        return f"Error al guardar los datos: {err}"
    finally:
        cursor.close()  # Cerrar el cursor después de la operación

@app.route('/reporteAsignatura')
def reporteAsignatura():
    try:
        cursor = db.cursor(dictionary=True)  # Usamos un cursor en modo diccionario para
        cursor.execute("SELECT * FROM asignatura")  # Cambiado a la tabla 'asign
        asignaturas = cursor.fetchall()  # Obtener todos los registros de asignaturas
        cursor.close()
        
        # Pasamos los registros de asignaturas a la plantilla 'reportAsignatura.html'
        return render_template('reporteAsignatura.html', asignaturas=asignaturas)
    except mysql.connector.Error as err:
        print(f"Error al consultar los datos: {err}")
        return "Error al consultar los datos"
    
    # Ruta para editar asignatura
@app.route('/editar_asignatura/<int:idasignatura>', methods=['GET', 'POST'])
def editar_asignatura(idasignatura):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        creditos = request.form.get('creditos')
        cuatrimestre = request.form.get('cuatrimestre')
        caracter = request.form.get('caracter')

        # Actualizar datos en la base de datos
        sql = """
        UPDATE asignatura
        SET nombre = %s, creditos = %s, cuatrimestre = %s, caracter = %s
        WHERE idasignatura = %s
        """
        valores = (nombre, creditos, cuatrimestre, caracter, idasignatura)
        
        try:
            cursor.execute(sql, valores)
            db.commit()
            return redirect(url_for('reporteAsignatura'))
        except mysql.connector.Error as err:
            db.rollback()
            return f"Error al actualizar la asignatura: {err}"
        finally:
            cursor.close()  # Cerrar cursor

    else:
        # Obtener datos de la asignatura para mostrarlos en el formulario
        cursor.execute("SELECT * FROM asignatura WHERE idasignatura = %s", (idasignatura,))
        asignatura = cursor.fetchone()
        cursor.close()
        
        if asignatura is None:
            print('Asignatura no encontrada', 'error')
            return redirect(url_for('reporteAsignatura'))  # Redirigir si la asignatura no existe
        
        return render_template('editarAsignatura.html', asignatura=asignatura)

# Ruta para eliminar asignatura
@app.route('/eliminar_asignatura/<int:idasignatura>', methods=['POST'])
def eliminar_asignatura(idasignatura):
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM asignatura WHERE idasignatura = %s", (idasignatura,))
        db.commit()
        return redirect(url_for('reporteAsignatura'))
    except mysql.connector.Error as err:
        db.rollback()
        return f"Error al eliminar la asignatura: {err}"
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
