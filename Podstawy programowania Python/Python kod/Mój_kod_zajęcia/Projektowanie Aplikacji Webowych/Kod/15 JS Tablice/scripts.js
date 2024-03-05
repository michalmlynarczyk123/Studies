let numerArray = [1, 2, 3]
let stringArray = ['one', 'two', 'three'];
let booleanArray = [false, true, false];
let mixArray = [1, "two", false]

console.log('Tablica numerArray')
console.log(numerArray)

console.log('Tablica stringArray')
console.log(stringArray)

console.log('Tablica booleanArray')
console.log(booleanArray)

console.log('Tablica mixArray')
console.log(mixArray)

console.log('Trzeci element z tablicy numericArray')
let n = numerArray[2];
console.log(n);

console.log('Tablica numericArray po modyfikacji drugiego elementu');
numerArray[1] = 100;
console.log(numerArray)

console.log('Element z tablicy numericArray spoza zakresu');
console.log(numerArray[-1])

console.log('Czy tablica numericArray zawiera liczbę 2?')
console.log(numerArray.includes(2))

console.log('Czy tablica numericArray zawiera liczbę 3?')
console.log(numerArray.includes(3))

console.log('Tablica stringArray po dodaniu nowego elementu');
stringArray.push('four');
console.log(stringArray)

console.log('Typ tablicy numericArray');
console.log(typeof numerArray)

console.log('Długość tablicy stringArray');
console.log(stringArray.length)