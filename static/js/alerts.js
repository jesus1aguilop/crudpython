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