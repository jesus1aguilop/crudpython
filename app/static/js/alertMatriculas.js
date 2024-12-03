// Función para validar y enviar formulario de Matrícula
function validarFormularioMatricula(event) {
    event.preventDefault();

    // Obtener valores de los campos
    const idalumno = document.getElementById('idalumno').value;
    const idasignatura = document.getElementById('idasignatura').value;

    // Validación de campos obligatorios
    if (!idalumno || !idasignatura) {
        Swal.fire({
            icon: 'warning',
            title: 'Selección Incompleta',
            text: 'Por favor, seleccione un alumno y una asignatura',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Entendido'
        });
        return;
    }

    // Confirmación de envío
    Swal.fire({
        title: 'Confirmar Matrícula',
        text: '¿Está seguro de registrar esta matrícula?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, registrar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                icon: 'success',
                title: 'Matrícula Registrada',
                text: 'La matrícula se ha registrado correctamente',
                showConfirmButton: false,
                timer: 1500
            });

            // Envío del formulario
            setTimeout(() => {
                document.getElementById('form_matricula').submit();
            }, 1600);
        }
    });
}