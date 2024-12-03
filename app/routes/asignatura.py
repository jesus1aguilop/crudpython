from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import app
from app.repositories.asignatura_repository import AsignaturaRepository
from flask_login import login_required

asignatura_bp = Blueprint('asignatura', __name__)

# Ruta para mostrar el formulario de creación de asignatura
asignatura_bp.route('/formulario3')
@login_required
def formulario3():
    return render_template('IngresoAsignatura.html')

# Ruta que recibe los datos del formulario de Asignatura
asignatura_bp.route('/submit_form3', methods=['POST'])
def submit_form3():
    nombre = request.form.get('nombre')
    creditos = request.form.get('creditos')
    cuatrimestre = request.form.get('cuatrimestre')
    caracter = request.form.get('caracter')

    # Usar el repositorio para crear una nueva asignatura
    asignatura = AsignaturaRepository.create_asignatura(nombre, creditos, cuatrimestre, caracter)

    if asignatura:
        flash('Asignatura creada con éxito', 'success')
        return redirect(url_for('formulario3'))
    else:
        flash('Error al crear la asignatura', 'error')
        return redirect(url_for('formulario3'))

# Ruta para mostrar los registros de las asignaturas
asignatura_bp.route('/reporteAsignatura')
@login_required
def reporteAsignatura():
    asignaturas = AsignaturaRepository.get_all_asignaturas()
    return render_template('reporteAsignatura.html', asignaturas=asignaturas)

# Ruta para eliminar una asignatura
asignatura_bp.route('/eliminar_asignatura/<int:idasignatura>', methods=["POST"])
def eliminar_asignatura(idasignatura):
    success = AsignaturaRepository.delete_asignatura(idasignatura)
    if success:
        flash('Asignatura eliminada con éxito', 'success')
    else:
        flash('Error al eliminar la asignatura', 'error')
    return redirect(url_for('reporteAsignatura'))

# Ruta para editar una asignatura
asignatura_bp.route('/editar_asignatura/<int:idasignatura>', methods=['GET', 'POST'])
@login_required
def editar_asignatura(idasignatura):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        creditos = request.form.get('creditos')
        cuatrimestre = request.form.get('cuatrimestre')
        caracter = request.form.get('caracter')

        # Usar el repositorio para actualizar la asignatura
        asignatura = AsignaturaRepository.update_asignatura(idasignatura, nombre, creditos, cuatrimestre, caracter)

        if asignatura:
            flash('Asignatura actualizada con éxito', 'success')
            return redirect(url_for('reporteAsignatura'))
        else:
            flash('Error al actualizar la asignatura', 'error')
            return redirect(url_for('editar_asignatura', idasignatura=idasignatura))

    else:
        # Obtener los datos de la asignatura a editar
        asignatura = AsignaturaRepository.get_asignatura_by_id(idasignatura)
        if not asignatura:
            flash('Asignatura no encontrada', 'error')
            return redirect(url_for('reporteAsignatura'))
        return render_template('editarAsignatura.html', asignatura=asignatura)
