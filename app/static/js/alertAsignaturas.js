// Función para validar y enviar formulario de Asignatura
function validarFormularioAsignatura(event) {
    event.preventDefault();

    // Obtener valores de los campos
    const nombre = document.getElementById('nombre').value;
    const creditos = document.getElementById('creditos').value;
    const cuatrimestre = document.getElementById('cuatrimestre').value;
    const caracter = document.getElementById('caracter').value;

    // Validación de campos obligatorios
    if (!nombre || !creditos || !cuatrimestre || !caracter) {
        Swal.fire({
            icon: 'warning',
            title: 'Campos Incompletos',
            text: 'Por favor, complete todos los campos de la asignatura',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Revisar'
        });
        return;
    }

    // Validación de créditos
    if (isNaN(creditos) || creditos <= 0) {
        Swal.fire({
            icon: 'error',
            title: 'Créditos Inválidos',
            text: 'Los créditos deben ser un número positivo',
            confirmButtonColor: '#d33',
            confirmButtonText: 'Corregir'
        });
        return;
    }

    // Confirmación de envío
    Swal.fire({
        icon: 'success',
        title: 'Formulario de Asignatura',
        text: 'Datos de asignatura guardados exitosamente',
        showConfirmButton: false,
        timer: 1500
    });

    // Envío del formulario
    setTimeout(() => {
        document.getElementById('form3').submit();
    }, 1600);
}
