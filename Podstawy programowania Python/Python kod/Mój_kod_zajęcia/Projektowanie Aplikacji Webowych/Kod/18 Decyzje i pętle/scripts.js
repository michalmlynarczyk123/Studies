// IF

let n = -5;

if (n > 0) {
    console.log('Większe od zera.');
} else if (n === 0) {
    console.log('Równe zero.');
} else {
    console.log('Mniejsze od zera.');
}

// For

for (let i = 0; i < 5; i++) {
    console.log(i)
}

let names = ['Jan', 'Adam', 'Andrzej'];

for (let name of names) {
    console.log(name)
}

// WHILE

let counter = 3;

while (counter < 3) {
    console.log(counter)
    counter++;
}

let counter2 = 3;

do {
    console.log(counter2)
} while (counter2 < 3)