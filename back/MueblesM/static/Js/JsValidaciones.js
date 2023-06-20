const form = document.getElementById('form');
const usuario = document.getElementById('username');
const usuario2 = document.getElementById('username2');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
	e.preventDefault();

	checkInputs();
});

function checkInputs() {
	// trim to remove the whitespaces
	const usuarioValue = usuario.value.trim();
    const usuario2Value = usuario2.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();

	if(usuarioValue === '') {
		setErrorFor(usuario, 'No puede dejar los Nombres en blanco');
	} else {
		setSuccessFor(usuario);
	}
    if(usuario2Value === '') {
		setErrorFor(usuario2, 'No puede dejar los Apellidos en blanco');
	} else {
		setSuccessFor(usuario2);
	}
	if(emailValue === '') {
		setErrorFor(email, 'No puede dejar el email en blanco');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'No ingreso un email válido');
	} else {
		setSuccessFor(email);
	}
    /*if(numberlValue === ''){
        setErrorFor(number, 'No ingreso ha ingresado un Numero Celular')
    }else if(numberValue > 999999999 && numberValue < 900000000 ){
        setErrorFor(number, 'El Numero debe tener 9 digitos y comenzar con un 9')
    }else{
		setSuccessFor(number);
	}*/

	if(passwordValue === '') {
		setErrorFor(password, 'La contraseña debe ser ingresada.');
	} else {
		setSuccessFor(password);
	}

	if(password2Value === '') {
		setErrorFor(password2, 'Se debe confirmar contraseña');
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2, 'las contraseñas no coinciden');
	} else{
		setSuccessFor(password2);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}