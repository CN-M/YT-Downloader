const email = document.getElementById('email');

email.addEventListener('input', (e) => {
    if (email.validity.typeMismatch) {
        email.setCustomValidity('I was expecting an e-mail address!');
        email.reportValidity();
    } else {
        email.setCustomValidity('');
    }
});

function showPassword() {
    let eye = document.getElementById('eye')
    let input = document.getElementById('password')
    if (input.type === 'password') {
        input.type = 'text';
    } else {
        input.type = 'password'
    }

    if ('fa-eye' == eye.classList[1]) {
        eye.classList.remove('fa-eye')
        eye.classList.add('fa-eye-slash')
    } else {
        eye.classList.remove('fa-eye-slash')
        eye.classList.add('fa-eye')
    }
    
}