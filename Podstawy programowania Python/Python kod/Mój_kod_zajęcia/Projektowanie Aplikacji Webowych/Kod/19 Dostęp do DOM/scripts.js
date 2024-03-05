window.onload = function() {
    /* Pojedyncze elementy */
    /*  ID */

    // document.getElementById('box-one').style.border = '3px solid green';

    /* SELEKTOR */

    // document.querySelector('#box-one').style.border = '3px solid green';

    // document.querySelector('.boxes').style.border = '3px solid green';

    /* WIELE ELEMENTÓW */

    /* KLASA */

   // let arr = document.getElementsByClassName('boxes');
   // for (let e of arr) {
   //     e.style.border = '3px solid green';
   // }

    /* NAZWY ZNACZNIKÓW */
   //  let arr = document.getElementsByTagName('div');
   //  for (let e of arr) {
   //     e.style.border = '3px solid green';
   // }

    /* SELEKTORY */

   //  let arr = document.querySelectorAll('#big-box div');
   //  for (let e of arr) {
   //     e.style.border = '3px solid green';
   // }

    /* PORUSZANIE SIĘ POMIĘDZY ELEMENTAMI */

    /* RODZIC */

    // document.getElementById('box-two').parentNode.style.border = '3px solid green';

    /* RODZEŃSTWO */

    // document.getElementById('box-two').previousElementSibling.style.border = '3px solid green'
    // document.getElementById('box-two').nextElementSibling.style.border = '3px solid green'

    /* DZIECKO */

    document.getElementById('big-box').firstElementChild.style.border = '3px solid green'
    document.getElementById('big-box').lastElementChild.style.border = '3px solid green'

};