from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repositories.matricula_repository import MatriculaRepository
from app.utils import login_required

matricula_bp = Blueprint('matricula', __name__, template_folder='../templates/matriculas')

# Ruta para mostrar el formulario de creación de matrícula
@matricula_bp.route('/matriculas')
@login_required
def matriculas():
    try:
        # Obtener lista de alumnos y asignaturas
        alumnos = MatriculaRepository.get_all_alumnos()
        asignaturas = MatriculaRepository.get_all_asignaturas()
        return render_template('ingresomatricula.html', alumnos=alumnos, asignaturas=asignaturas)
    except Exception as e:
        print(f"Error al cargar datos: {e}", 'error')
        return redirect(url_for('matricula.reporte_matriculas'))

# Ruta que recibe los datos del formulario de matrícula
@matricula_bp.route('/submit_matricula', methods=['POST'])
def submit_matricula():
    # Obtener lista de alumnos y asignaturas
    alumnos = MatriculaRepository.get_all_alumnos()
    asignaturas = MatriculaRepository.get_all_asignaturas()
    
    idalumno = request.form.get('idalumno')
    idasignatura = request.form.get('idasignatura')

    if not idalumno or not idasignatura:
        print("Debe seleccionar un alumno y una asignatura", 'error')
        return redirect(url_for('matricula.matriculas', alumnos=alumnos, asignaturas=asignaturas))

    try:
        # Usar el repositorio para crear una nueva matrícula
        success = MatriculaRepository.create_matricula(idalumno, idasignatura)
        
        if success:
            print('Matrícula creada con éxito', 'success')
        else:
            print('Error al crear la matrícula', 'error')
            
        return redirect(url_for('matricula.reporte_matriculas'))
    except Exception as e:
        print(f"Error al registrar matrícula: {e}", 'error')
        return redirect(url_for('matricula.matriculas'))

# Ruta para mostrar los registros de las matrículas
@matricula_bp.route('/reporte_matriculas')
@login_required
def reporte_matriculas():
    try:
        matriculas = MatriculaRepository.get_all_matriculas()
        return render_template('reportematricula.html', matriculas=matriculas)
    except Exception as e:
        print(f"Error al cargar matrículas: {e}", 'error')
        return redirect(url_for('matricula.matriculas'))

# Ruta para eliminar una matrícula
@matricula_bp.route('/eliminar_matricula/<int:idmatricula>', methods=['POST'])
def eliminar_matricula(idmatricula):
    try:
        success = MatriculaRepository.delete_matricula(idmatricula)
        
        if success:
            print('Matrícula eliminada con éxito', 'success')
        else:
            print('Error al eliminar la matrícula', 'error')
        
        return redirect(url_for('matricula.reporte_matriculas'))
    except Exception as e:
        print(f"Error al eliminar matrícula: {e}", 'error')
        return redirect(url_for('matricula.reporte_matriculas'))

# Ruta para editar una matrícula
@matricula_bp.route('/editar_matricula/<int:idmatricula>', methods=['GET', 'POST'])
@login_required
def editar_matricula(idmatricula):
    try:
        if request.method == 'POST':
            idalumno = request.form.get('idalumno')
            idasignatura = request.form.get('idasignatura')

            if not idalumno or not idasignatura:
                print("Debe seleccionar un alumno y una asignatura", 'error')
                return redirect(url_for('matricula.editar_matricula', idmatricula=idmatricula))

            # Usar el repositorio para actualizar la matrícula
            success = MatriculaRepository.update_matricula(idmatricula, idalumno, idasignatura)

            if success:
                print('Matrícula actualizada con éxito', 'success')
                return redirect(url_for('matricula.reporte_matriculas'))
            else:
                print('Error al actualizar la matrícula', 'error')
                return redirect(url_for('matricula.editar_matricula', idmatricula=idmatricula))

        else:
            matricula = MatriculaRepository.get_matricula_by_id(idmatricula)
            if not matricula:
                print('Matrícula no encontrada', 'error')
                return redirect(url_for('matricula.reporte_matriculas'))

            alumnos = MatriculaRepository.get_all_alumnos()
            asignaturas = MatriculaRepository.get_all_asignaturas()

            return render_template('editarmatricula.html', matricula=matricula, alumnos=alumnos, asignaturas=asignaturas)
    
    except Exception as e:
        print(f"Error al editar matrícula: {e}", 'error')
        return redirect(url_for('matricula.reporte_matriculas'))
