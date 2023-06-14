// object er svipað klass

let car = {
    make: 'bmw',
    model: '745i',
    year: 2010,

    // þessi function kallast method útaf þau eru inn í object
    getPrice: function() {
        //Perform some calc
        return 5000;
    },
    printDescription: function() {
        console.log(this.make + ' ' + this.model);
    }
}

car.printDescription();
// þetta er rétta leiðin að ná í upplýsingar inn í object
console.log(car.year);

console.log(car);

/*
// ekki gera þetta
console.log(car['year']);
console.log(car[0]);
*/



// breyta með slaufusviga er object. inní slaufuna koma upplýsingarnar
// eða functions sem skal nota inn í objectinu.
var anotherCar = {};
anotherCar.whatever = 'bob';
console.log(anotherCar.whatever);


var a = {
    myProperty: { b: 'hi'}
};
console.log(a.myProperty.b);

// kassasvigi er array eða listi -- inn í array er hægt að geyma upplýsingar
var breyta = {
    myProperty2: [
        { d: 'this'},
        { e: 'can'},
        { f: 'get'},
        { g: 'crazy'}
    ]
};

console.log(breyta.myProperty2[1].e);

let contacts = {
    customers: [
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
    ],
    employees: [
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
        { firstname: 'bob', lastname: 'tabor', phonenumbers: ['símanúmer1','símanúmer2']},
    ]
}

console.log(contacts.customers[1].firstname)