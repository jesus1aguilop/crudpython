function validarDatos(event){
    event.preventDefault();//evitar error al mostrar el alert 

    //verificacion de los datos
    const nombre = document.getElementById('nombre').value;
    const apellidos = document.getElementById('apellidos').value;
    const direccion_postal = document.getElementById('direccion_postal').value;
    const direccion_electronica = document.getElementById('direccion_electronica').value;
    const tiene_beca = document.getElementById('tiene_beca').checked;

    if(!nombre || !apellidos || !direccion_postal || !direccion_electronica){
        Swal.fire({
            position: "top-end",
            icon: "warning",
            title: "formulario incompleto",
            showConfirmButton: false,
            timer: 1500
        });
        return 
    }

    Swal.fire({
        position: "top-end",
        icon: "success",
        title: "Formulario enviado correctamente",
        showConfirmButton: false,
        timer: 1500
    });

// Espera a que el alert termine y envía el formulario
setTimeout(() => {
    document.getElementById('form').submit(); // Reemplaza 'miFormulario' con el ID de tu formulario
}, 1600); // Se espera un poco más de 1500 ms para asegurarse de que el alert termine

}
