from flask import Blueprint, request, render_template, redirect, url_for
from app.repositories.alumno_repository import AlumnoRepository

alumno_bp = Blueprint('alumno', __name__)

# Ruta para mostrar el formulario de ingreso de alumnos
@alumno_bp.route('/formulario')
def formulario():
    return render_template('/templates/alumnos/IngresoAlumno.html')

# Ruta para recibir los datos del formulario y crear un alumno
@alumno_bp.route('/submit_form', methods=['POST'])
def submit_form():
    datos = request.form
    try:
        AlumnoRepository.crear_alumno(
            nombre=datos.get('nombre'),
            apellidos=datos.get('apellidos'),
            direccion_postal=datos.get('direccion_postal'),
            direccion_electronica=datos.get('direccion_electronica'),
            tiene_beca=datos.get('tiene_beca') == 'on'
        )
        return redirect(url_for('alumno.reporte'))
    except Exception as e:
        return f"Error al guardar los datos: {e}"

# Ruta para mostrar un reporte con todos los alumnos
@alumno_bp.route('/reporte')
def reporte():
    try:
        alumnos = AlumnoRepository.obtener_todos_los_alumnos()
        return render_template('/templates/alumnos/reportAlumno.html', alumnos=alumnos)
    except Exception as e:
        return f"Error al consultar los datos: {e}"

# Ruta para mostrar el formulario de edición de un alumno
@alumno_bp.route('/editar_alumno/<int:idalumno>', methods=['GET', 'POST'])
def editar_alumno(idalumno):
    if request.method == 'POST':
        datos = request.form
        try:
            AlumnoRepository.actualizar_alumno(
                idalumno=idalumno,
                nombre=datos.get('nombre'),
                apellidos=datos.get('apellidos'),
                direccion_postal=datos.get('direccion_postal'),
                direccion_electronica=datos.get('direccion_electronica'),
                tiene_beca=datos.get('tiene_beca') == 'on'
            )
            return redirect(url_for('alumno.reporte'))
        except Exception as e:
            return f"Error al actualizar el alumno: {e}"
    else:
        alumno = AlumnoRepository.obtener_alumno_por_id(idalumno)
        if not alumno:
            return redirect(url_for('alumno.reporte'))
        return render_template('/templates/alumnos/editarAlumno.html', alumno=alumno)

# Ruta para eliminar un alumno
@alumno_bp.route('/eliminar_alumno/<int:idalumno>', methods=['POST'])
def eliminar_alumno(idalumno):
    try:
        AlumnoRepository.eliminar_alumno(idalumno)
        return redirect(url_for('alumno.reporte'))
    except Exception as e:
        return f"Error al eliminar el alumno: {e}"
