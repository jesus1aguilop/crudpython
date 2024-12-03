// Función para validar y enviar formulario de Curso
function validarFormularioCurso(event) {
    event.preventDefault();

    // Obtener valores de los campos
    const nombre = document.getElementById('nombre').value;
    const numero_asignaturas = document.getElementById('numero_asignaturas').value;

    // Validación de campos obligatorios
    if (!nombre || !numero_asignaturas) {
        Swal.fire({
            icon: 'warning',
            title: 'Campos Incompletos',
            text: 'Por favor, complete el nombre y número de asignaturas',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Entendido'
        });
        return;
    }

    // Validación de número de asignaturas
    if (isNaN(numero_asignaturas) || numero_asignaturas <= 0) {
        Swal.fire({
            icon: 'error',
            title: 'Número Inválido',
            text: 'El número de asignaturas debe ser un valor positivo',
            confirmButtonColor: '#d33',
            confirmButtonText: 'Corregir'
        });
        return;
    }

    // Confirmación de envío
    Swal.fire({
        icon: 'success',
        title: 'Formulario de Curso',
        text: 'Datos de curso guardados correctamente',
        showConfirmButton: false,
        timer: 1500
    });

    // Envío del formulario
    setTimeout(() => {
        document.getElementById('form2').submit();
    }, 1600);
}
