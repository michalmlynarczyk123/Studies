window.onload = function () {

    const MIN_EMAIL_LENGTH = 8
    const MIN_PASSWORD_LENGTH = 8;

    let userForm = document.getElementById('user-form');

    let emailInput = document.getElementById('email');
    let emailError = document.getElementById('email-error');

    let passwordInput = document.getElementById('password');
    let passwordError = document.getElementById('password-error');

    userForm.addEventListener('submit', function (e) {
        e.preventDefault();

        if (validateForm()) {
            console.log('Poprawnie wysłany formularz');
            console.log(`Adres email: ${emailInput.value}`);
            console.log(`Hasło: ${passwordInput.value}`);
            clearForm()
        }
    })

    function validateForm() {
        let validEmail = true;
        let validPassword = true;

        if (emailInput.value.length < MIN_EMAIL_LENGTH) {
            validEmail = false;
            emailError.removeAttribute('hidden');
        } else {
            emailError.setAttribute('hidden', '')
        }

        if (passwordInput.value.length < MIN_PASSWORD_LENGTH) {
            validPassword = false;
            passwordError.removeAttribute('hidden');
        } else {
            passwordError.setAttribute('hidden', '')
        }

        return validEmail && validPassword;
    }

    function clearForm(){
        emailInput.value = '';
        passwordInput.value = '';
    }

};