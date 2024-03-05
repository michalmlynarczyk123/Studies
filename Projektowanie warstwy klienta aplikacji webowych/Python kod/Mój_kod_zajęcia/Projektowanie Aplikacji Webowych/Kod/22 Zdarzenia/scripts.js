window.onload = function () {

    // Kliknięcie + klawisze
    let clickCounter = 0;
    let doubleClickCounter = 0;
    let keyDownCounter = 0;

    document.getElementById('click-counter-value').textContent = clickCounter
    document.getElementById('double-click-counter-value').textContent = doubleClickCounter;
    document.getElementById('key-down-counter-value').textContent = keyDownCounter;

    document.addEventListener('click', function (){
        clickCounter = clickCounter + 1;
        document.getElementById('click-counter-value').textContent = clickCounter;
    });

    document.addEventListener('dblclick', function (){
       document.getElementById('double-click-counter-value').textContent = ++doubleClickCounter;
    });

    document.addEventListener('keydown', function (){
       document.getElementById('key-down-counter-value').textContent = ++keyDownCounter;
    });

//     Pudełka

    let button = document.getElementById('add-element');
    let boxContainer = document.getElementById('box-container');

    button.addEventListener('click', function (){
        let newElement = document.createElement('div');
        newElement.classList.add('box')
        boxContainer.appendChild(newElement);
    })

    boxContainer.addEventListener('click', function (e){
        if (e.target.className.includes('box')) {
            this.removeChild(e.target);
        }
    })


};