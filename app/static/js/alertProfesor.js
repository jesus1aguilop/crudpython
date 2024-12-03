// Función para validar y enviar formulario de Profesor
function validarFormularioProfesor(event) {
    event.preventDefault();

    // Obtener valores de los campos
    const nif = document.getElementById('nif').value;
    const nombre = document.getElementById('nombre').value;
    const apellidos = document.getElementById('apellidos').value;
    const telefono = document.getElementById('telefono').value;
    const direccion_postal = document.getElementById('direccion_postal').value;
    const direccion_electronica = document.getElementById('direccion_electronica').value;
    const categoria = document.getElementById('categoria').value;

    // Validación de campos obligatorios
    const camposObligatorios = [nif, nombre, apellidos, telefono, direccion_postal, direccion_electronica, categoria];
    if (camposObligatorios.some(campo => !campo)) {
        Swal.fire({
            icon: 'warning',
            title: 'Campos Incompletos',
            text: 'Por favor, complete todos los campos del formulario de profesor',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Revisar'
        });
        return;
    }

    // Validación de NIF/NIE
    const nifRegex = /^[XYZ]?\d{7,8}[A-HJ-NP-TV-Z]$/i;
    if (!nifRegex.test(nif)) {
        Swal.fire({
            icon: 'error',
            title: 'NIF/NIE Inválido',
            text: 'Por favor, ingrese un NIF/NIE válido',
            confirmButtonColor: '#d33',
            confirmButtonText: 'Corregir'
        });
        return;
    }

    // Confirmación de envío
    Swal.fire({
        icon: 'success',
        title: 'Formulario de Profesor',
        text: 'Datos de profesor guardados exitosamente',
        showConfirmButton: false,
        timer: 1500
    });

    // Envío del formulario
    setTimeout(() => {
        document.getElementById('form1').submit();
    }, 1600);
}
