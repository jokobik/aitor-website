const passInput = document.getElementById('login-password');
const btnMostrar = document.getElementById('login-mostrar');

btnMostrar.addEventListener('click', () => {
    if (passInput.type === 'password') {
        passInput.type = 'text';
        btnMostrar.classList.add('barra'); // Añade barra
    } else {
        passInput.type = 'password';
        btnMostrar.classList.remove('barra'); // Quita barra
    }
});