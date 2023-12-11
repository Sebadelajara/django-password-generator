// const $username = document.getElementById('username');


// // validaciones de inputs

const formulario = document.getElementById('formsignup');
const inputs = document.querySelectorAll('#formsignup input');

// //expresiones regulares

const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,30}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,50}$/, // Letras y espacios, pueden llevar acentos.
    password: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{4,12}$/, // 4 a 12 digitos.
    confirm_password: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{4,12}$/, // 4 a 12 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
}

const campos = {
    usuario: false,
    firstname: false,
    lastname: false,
    password: false,
    email: false
}


const validarForm = (e) => {
    switch (e.target.name) {
        case "username":
            validarCampo(expresiones.usuario, e.target, 'usuario');
            break;
        case "firstname":
            validarCampo(expresiones.nombre, e.target, 'firstname');
            break;
        case "lastname":
            validarCampo(expresiones.apellido, e.target, 'lastname');
            break;
        case "password":
            validarCampo(expresiones.password, e.target, 'password');
            validarPassword2();
            break;
        case "confirm_password":
            validarPassword2();
            break;
        case "email":
            validarCampo(expresiones.correo, e.target, 'email');
            break;
    }
}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`grupo-${campo}`).classList.remove('form-grupo-incorrecto');
        document.getElementById(`grupo-${campo}`).classList.add('form-grupo-correcto');
        document.querySelector(`#grupo-${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo-${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo-${campo} .formulario-input-error`).classList.remove('formulario-input-error-activo');
        campos[campo] = true;
    } else {
        document.getElementById(`grupo-${campo}`).classList.add('form-grupo-incorrecto');
        document.getElementById(`grupo-${campo}`).classList.remove('form-grupo-correcto');
        document.querySelector(`#grupo-${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo-${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo-${campo} .formulario-input-error`).classList.add('formulario-input-error-activo');
        campos[campo] = false;
    }
}



const validarPassword2 = () => {
    const inputPassword1 = document.getElementById('password');
    const inputPassword2 = document.getElementById('confirm_password');

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById(`grupo-confirm-password`).classList.add('form-grupo-incorrecto');
        document.getElementById(`grupo-confirm-password`).classList.remove('form-grupo-correcto');
        document.querySelector(`#grupo-confirm-password i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo-confirm-password i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo-confirm-password .formulario-input-error`).classList.add('formulario-input-error-activo');
        campos['password'] = false;
    } else {
        document.getElementById(`grupo-confirm-password`).classList.remove('form-grupo-incorrecto');
        document.getElementById(`grupo-confirm-password`).classList.add('form-grupo-correcto');
        document.querySelector(`#grupo-confirm-password i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo-confirm-password i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo-confirm-password .formulario-input-error`).classList.remove('formulario-input-error-activo');
        campos['password'] = true;
    }
}





inputs.forEach((input) => {
    input.addEventListener('keyup', validarForm);
    input.addEventListener('blur', validarForm);
});


// e.preventDefault(); //no envia datos al backend

// formulario.addEventListener('submit', (e) => {


//     const terminos = document.getElementById('terminos');
//     if (campos.usuario && campos.firstname && campos.lastname && campos.password && campos.email && terminos.checked) {
//         formulario.reset();

//         document.querySelectorAll('.form-grupo-correcto').forEach((icono) => {
//             icono.classList.remove('form-grupo-correcto');
//         })
//     } else {
//         document.getElementById('form-mensaje').classList.add('form-mensaje-activo');
//         setTimeout(() => {
//             document.getElementById('form-mensaje').classList.remove('form-mensaje-activo');
//         }, 5000);
//     }
// });











// confirmacion de password

