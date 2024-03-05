function simpleFunction(){
    console.log('Prosta funcja')
}

simpleFunction();

function rewriteIt(text) {
    console.log(text);
}

rewriteIt('Mam na imię Michał')

function sumOfTwo(a, b) {
    let sum = a + b
    console.log(`${a} + ${b} = ${sum}`)
}

sumOfTwo(2,3 )


function functionWithReturn() {
    return 'Zwrócona wartość'
}

console.log(functionWithReturn())

function showReturned(){
    let text = functionWithReturn();
    console.log(text)
}

showReturned()