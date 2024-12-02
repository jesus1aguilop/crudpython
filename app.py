from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="universidad_2"
)

# Función para verificar si el usuario está logueado (decorador)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debe iniciar sesión para acceder a esta página.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ---------------------------
# Funciones de Login y Registro
# ---------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            cursor = db.cursor(dictionary=True)

            # Verificar si el usuario existe en la base de datos
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()

            cursor.close()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['idusuario']
                session['user_name'] = user['username']
                flash('Inicio de sesión exitoso.', 'success')
                return redirect(url_for('index'))
            else:
                flash('Usuario o contraseña incorrectos.', 'danger')
                return redirect(url_for('login'))
        except mysql.connector.Error as err:
            print(f"Error al consultar la base de datos: {err}")
            flash('Error en la base de datos.', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Ruta para el registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        try:
            cursor = db.cursor()

            # Verificar si el usuario ya existe
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('El usuario ya existe.', 'danger')
                cursor.close()
                return redirect(url_for('registro'))

            # Guardar nuevo usuario en la base de datos
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            db.commit()
            cursor.close()

            flash('Usuario registrado exitosamente.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            print(f"Error al registrar el usuario: {err}")
            flash('Error en la base de datos.', 'danger')
            return redirect(url_for('registro'))

    return render_template('registro.html')

# Resto de tu aplicación...


@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada exitosamente', 'success')
    return redirect(url_for('login'))

# ---------------------------
# Código existente (resumido)
# ---------------------------

@app.route('/')
@login_required
def index():
    if 'user_id' in session:
        return render_template('index.html', user_name=session['user_name'])
    flash('Por favor, inicia sesión primero', 'error')
    return redirect(url_for('login'))

# endpoint del formulario de Alumno
@app.route('/formulario')
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
            cursor.execute("""  # Ensure the table name is correct
                UPDATE curso  
                SET nombre = %s, numero_asignaturas = %s
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
        cursor.execute("SELECT * FROM curso WHERE idcurso = %s", (idcurso,))
        curso = cursor.fetchone()  
        cursor.close()
        
        if curso is None:
            print('Curso no encontrado', 'error')
            return redirect(url_for('reporteCurso'))  
        
        return render_template('editarCurso.html', curso=curso)

@app.route('/formulario3')
@login_required
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
@login_required
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
        
# Ruta para mostrar el formulario de matrícula
@app.route('/matriculas', methods=['GET'])
@login_required
def matriculas():
    try:
        cursor = db.cursor(dictionary=True)

        # Consultar estudiantes
        cursor.execute("SELECT idalumno, nombre, apellidos FROM alumnos")
        alumnos = cursor.fetchall()

        # Consultar asignaturas
        cursor.execute("SELECT idasignatura, nombre FROM asignatura")
        asignaturas = cursor.fetchall()

        cursor.close()
        return render_template('ingresomatricula.html', alumnos=alumnos, asignaturas=asignaturas)
    except mysql.connector.Error as err:
        print(f"Error al cargar datos: {err}")
        return "Error al cargar datos para matrícula"


# Ruta para registrar una nueva matrícula
@app.route('/registrar_matricula', methods=['POST'])
def registrar_matricula():
    try:
        idalumno = request.form.get('idalumno')
        idasignatura = request.form.get('idasignatura')

        if not idalumno or not idasignatura:
            return "Debe seleccionar un alumno y una asignatura"

        # Usar mysql.connector para insertar la matrícula
        cursor = db.cursor()
        consulta = "INSERT INTO matricula (idalumno, idasignatura) VALUES (%s, %s)"
        cursor.execute(consulta, (idalumno, idasignatura))
        db.commit()
        cursor.close()

        return redirect(url_for('reporte_matriculas'))
    except mysql.connector.Error as err:
        db.rollback()
        print(f"Error al registrar matrícula: {err}")
        return f"Error al registrar matrícula: {err}"


# Ruta para listar matrículas
@app.route('/reporte_matriculas')
@login_required
def reporte_matriculas():
    try:
        cursor = db.cursor(dictionary=True)

        consulta = """
            SELECT m.idmatricula, 
                   a.nombre AS alumno_nombre, 
                   a.apellidos AS alumno_apellidos,
                   asig.nombre AS asignatura_nombre
            FROM matricula m
            JOIN alumnos a ON m.idalumno = a.idalumno
            JOIN asignatura asig ON m.idasignatura = asig.idasignatura
        """
        cursor.execute(consulta)
        matriculas = cursor.fetchall()
        cursor.close()

        return render_template('reportematricula.html', matriculas=matriculas)
    except mysql.connector.Error as err:
        print(f"Error al consultar matrículas: {err}")
        return f"Error al consultar matrículas: {err}"
    # Ruta para eliminar matrícula
@app.route('/eliminar_matricula/<int:idmatricula>', methods=['POST'])
def eliminar_matricula(idmatricula):
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM matricula WHERE idmatricula = %s", (idmatricula,))
        db.commit()
        cursor.close()

        return redirect(url_for('reporte_matriculas'))
    except mysql.connector.Error as err:
        db.rollback()
        print(f"Error al eliminar matrícula: {err}")
        return f"Error al eliminar matrícula: {err}"

# Ruta para editar matrícula
@app.route('/editar_matricula/<int:idmatricula>', methods=['GET', 'POST'])
def editar_matricula(idmatricula):
    try:
        cursor = db.cursor(dictionary=True)

        if request.method == 'GET':
            # Consultar los detalles de la matrícula
            cursor.execute("""
                SELECT idmatricula, idalumno, idasignatura 
                FROM matricula 
                WHERE idmatricula = %s
            """, (idmatricula,))
            matricula = cursor.fetchone()

            # Consultar alumnos y asignaturas
            cursor.execute("SELECT idalumno, nombre, apellidos FROM alumnos")
            alumnos = cursor.fetchall()

            cursor.execute("SELECT idasignatura, nombre FROM asignatura")
            asignaturas = cursor.fetchall()

            cursor.close()
            return render_template('editarmatricula.html', matricula=matricula, alumnos=alumnos, asignaturas=asignaturas)

        elif request.method == 'POST':
            idalumno = request.form.get('idalumno')
            idasignatura = request.form.get('idasignatura')

            try:
                # Validar que los datos existan
                cursor.execute("SELECT COUNT(*) AS count FROM alumnos WHERE idalumno = %s", (idalumno,))
                if cursor.fetchone()['count'] == 0:
                    raise ValueError("El alumno seleccionado no existe.")

                cursor.execute("SELECT COUNT(*) AS count FROM asignatura WHERE idasignatura = %s", (idasignatura,))
                if cursor.fetchone()['count'] == 0:
                    raise ValueError("La asignatura seleccionada no existe.")

                # Actualizar matrícula
                consulta = """
                UPDATE matricula 
                SET idalumno = %s, idasignatura = %s 
                WHERE idmatricula = %s
                """
                cursor.execute(consulta, (idalumno, idasignatura, idmatricula))
                db.commit()
                cursor.close()

                return redirect(url_for('reporte_matriculas'))
            except Exception as e:
                db.rollback()
                print(f"Error al editar matrícula: {e}")
                return f"Error al editar matrícula: {e}"

    except Exception as e:
        print(f"Error en la consulta inicial: {e}")
        return f"Error en la consulta inicial: {e}"


if __name__ == '__main__':
    app.run(debug=True)
