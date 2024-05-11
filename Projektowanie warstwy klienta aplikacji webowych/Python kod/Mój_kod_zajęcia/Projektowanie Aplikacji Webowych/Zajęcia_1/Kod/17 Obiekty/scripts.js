// Notacja literałów

let person = {
    firstName: 'Jan',
    lastName: 'Kowalski',
    introduce: function (){
        console.log(`Nazywam się ${this.firstName} ${this.lastName}`)
    },
}

person.introduce()
person.firstName = 'Adam';
person.introduce()

// Notacja konstruktora

function Car(brandVal, modelVal){
    this.brand = brandVal;
    this.model = modelVal;

    this.showDetails = function (){
        console.log(`Car: ${this.brand} ${this.model}`)
    };
}

let fiat = new Car('fiat', '126p')
fiat.showDetails()

// Przez Klasę

class House {
    constructor(windowsValue, doorsValue){
        this.windows = windowsValue
        this.doors = doorsValue
    }

    showDetails(){
        console.log(`Dom ma: ${this.windows} okien oraz ${this.doors} drzwi.`);
    }
}

let house1 = new House(2,6);
house1.showDetails();