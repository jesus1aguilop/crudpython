from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repositories.curso_repository import CursoRepository
from app.utils import login_required

curso_bp = Blueprint('curso', __name__, template_folder='../templates/cursos')

# Ruta para mostrar el formulario de creación de curso
@curso_bp.route('/formulario2')
@login_required
def formulario2():
    return render_template('IngresoCurso.html')

# Ruta que recibe los datos del formulario de Curso
@curso_bp.route('/submit_form2', methods=['POST'])
def submit_form2():
    nombre = request.form.get('nombre')
    numero_asignaturas = request.form.get('numero_asignaturas')

    # Usar el repositorio para crear un nuevo curso
    curso = CursoRepository.create_curso(nombre, numero_asignaturas)

    if curso:
        flash('Curso creado con éxito', 'success')
        return redirect(url_for('curso.formulario2'))
    else:
        flash('Error al crear el curso', 'error')
        return redirect(url_for('curso.formulario2'))

# Ruta para mostrar los registros de los cursos
@curso_bp.route('/reporteCurso')
@login_required
def reporteCurso():
    cursos = CursoRepository.get_all_cursos()
    return render_template('reportCurso.html', cursos=cursos)

# Ruta para eliminar un curso
@curso_bp.route('/eliminar_curso/<int:idcurso>', methods=["POST"])
def eliminar_curso(idcurso):
    success = CursoRepository.delete_curso(idcurso)
    if success:
        flash('Curso eliminado con éxito', 'success')
    else:
        flash('Error al eliminar el curso', 'error')
    return redirect(url_for('curso.reporteCurso'))

# Ruta para editar un curso
@curso_bp.route('/editar_curso/<int:idcurso>', methods=['GET', 'POST'])
@login_required
def editar_curso(idcurso):
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        numero_asignaturas = request.form.get('numero_asignaturas')

        # Usar el repositorio para actualizar el curso
        curso = CursoRepository.update_curso(idcurso, nombre, numero_asignaturas)

        if curso:
            flash('Curso actualizado con éxito', 'success')
            return redirect(url_for('curso.reporteCurso'))
        else:
            flash('Error al actualizar el curso', 'error')
            return redirect(url_for('curso.editar_curso', idcurso=idcurso))

    else:
        # Obtener el curso a editar
        curso = CursoRepository.get_curso_by_id(idcurso)
        if not curso:
            flash('Curso no encontrado', 'error')
            return redirect(url_for('curso.reporteCurso'))
        return render_template('editarCurso.html', curso=curso)
