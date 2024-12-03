from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import app
from app.repositories.profesor_repository import ProfesorRepository
from flask_login import login_required

profesor_bp = Blueprint('profesor', __name__)

# Ruta para mostrar el formulario de creación de profesor
profesor_bp.route('/formulario1')
@login_required
def formulario1():
    return render_template('IngresoProfesor.html')

# Ruta que recibe los datos del formulario de Profesor
profesor_bp.route('/submit_form1', methods=['POST'])
def submit_form1():
    nif = request.form.get('nif')
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    telefono = request.form.get('telefono')
    direccion_postal = request.form.get('direccion_postal')   
    direccion_electronica = request.form.get('direccion_electronica')
    categoria = request.form.get('categoria')

    # Usar el repositorio para crear un nuevo profesor
    profesor = ProfesorRepository.create_profesor(
        nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria
    )

    if profesor:
        flash('Profesor creado con éxito', 'success')
        return redirect(url_for('formulario1'))
    else:
        flash('Error al crear el profesor', 'error')
        return redirect(url_for('formulario1'))

# Ruta para mostrar los registros de los profesores
profesor_bp.route('/reporteProfesor')
@login_required
def reporteProfesor():
    profesores = ProfesorRepository.get_all_profesores()
    return render_template('reporteProfesor.html', profesores=profesores)

# Ruta para eliminar un profesor
profesor_bp.route('/eliminar_profesor/<int:idprofesor>', methods=["POST"])
def eliminar_profesor(idprofesor):
    success = ProfesorRepository.delete_profesor(idprofesor)
    if success:
        flash('Profesor eliminado con éxito', 'success')
    else:
        flash('Error al eliminar el profesor', 'error')
    return redirect(url_for('reporteProfesor'))

# Ruta para editar un profesor
profesor_bp.route('/editar_profesor/<int:idprofesor>', methods=['GET', 'POST'])
@login_required
def editar_profesor(idprofesor):
    if request.method == 'POST':
        nif = request.form.get('nif')
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        telefono = request.form.get('telefono')
        direccion_postal = request.form.get('direccion_postal')   
        direccion_electronica = request.form.get('direccion_electronica')
        categoria = request.form.get('categoria')

        # Usar el repositorio para actualizar el profesor
        profesor = ProfesorRepository.update_profesor(
            idprofesor, nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria
        )

        if profesor:
            flash('Profesor actualizado con éxito', 'success')
            return redirect(url_for('reporteProfesor'))
        else:
            flash('Error al actualizar el profesor', 'error')
            return redirect(url_for('editar_profesor', idprofesor=idprofesor))

    else:
        # Obtener el profesor a editar
        profesor = ProfesorRepository.get_profesor_by_id(idprofesor)
        if not profesor:
            flash('Profesor no encontrado', 'error')
            return redirect(url_for('reporteProfesor'))
        return render_template('editarProfesor.html', profesor=profesor)
