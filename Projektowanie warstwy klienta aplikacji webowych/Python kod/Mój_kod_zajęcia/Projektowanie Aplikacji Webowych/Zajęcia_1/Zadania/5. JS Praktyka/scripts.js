window.onload = function () {

    const MIN_LENGTH = 3;

    let userForm = document.getElementById('user-form');
    let userInput = document.getElementById('user');
    let userError = document.getElementById('user-error');
    let addUser = document.getElementById('add')


    userForm.addEventListener('submit', function (e) {
        e.preventDefault();
        let newUser = document.createElement('p')
        newUser.classList.add('p1')
        newUser.textContent = userInput.value;
        addUser.appendChild(newUser)

        if (validateForm()) {
            // console.log('Poprawnie dodano pracownika')
            // console.log(`Imię i nazwisko prawcownika: ${userInput.value}`)
            clearForm()
        }
    })
    function validateForm() {
        let validUser = true;

        if (userInput.value.length < MIN_LENGTH) {
            validUser = false;
            userError.removeAttribute('hidden')
        } else {
            userError.setAttribute('hidden', '')
        }

        return validUser;
    }

    function clearForm(){
        userInput.value = ''
    }

};