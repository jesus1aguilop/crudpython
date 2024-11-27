// Función para validar y enviar formulario de Alumno
function validarFormularioAlumno(event) {
    event.preventDefault();

    // Obtener valores de los campos
    const nombre = document.getElementById('nombre').value;
    const apellidos = document.getElementById('apellidos').value;
    const direccion_postal = document.getElementById('direccion_postal').value;
    const direccion_electronica = document.getElementById('direccion_electronica').value;
    const tiene_beca = document.getElementById('tiene_beca').checked;

    // Validación de campos obligatorios
    if (!nombre || !apellidos || !direccion_postal || !direccion_electronica) {
        Swal.fire({
            icon: 'warning',
            title: 'Campos Incompletos',
            text: 'Por favor, complete todos los campos obligatorios',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Entendido'
        });
        return;
    }

    // Validación de correo electrónico
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(direccion_electronica)) {
        Swal.fire({
            icon: 'error',
            title: 'Correo Electrónico Inválido',
            text: 'Por favor, ingrese un correo electrónico válido',
            confirmButtonColor: '#d33',
            confirmButtonText: 'Corregir'
        });
        return;
    }

    // Confirmación de envío
    Swal.fire({
        icon: 'success',
        title: 'Formulario de Alumno',
        text: 'Datos guardados correctamente',
        showConfirmButton: false,
        timer: 1500
    });

    // Envío del formulario
    setTimeout(() => {
        document.getElementById('form').submit();
    }, 1600);
}
