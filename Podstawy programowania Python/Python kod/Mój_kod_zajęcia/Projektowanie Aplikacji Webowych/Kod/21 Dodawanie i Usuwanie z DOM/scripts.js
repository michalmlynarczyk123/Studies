window.onload = function () {
    setTimeout( function (){
        let element = document.createElement('div');
        element.textContent = '5'

        document.getElementById('big-box').appendChild(element)
    }, 2000)

    setTimeout(function (){
        let element = document.getElementById('box-two');
        let parent = document.getElementById('big-box');

        parent.removeChild(element)


    }, 5000);
};