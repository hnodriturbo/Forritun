var myVariable = 'I am at the global scope';

var myFunction = function() {
    console.log('me too!');
}
console.log(myVariable)
myFunction()

// Skilgreini function one() og opna kóðablokk sem return string 'one'
function one() {
    return 'one';
}
// set functionið inn í breytu. return value úr function verður að breytunni
let value = one();
// keyri breytuna
console.log(value);

let value2 = one();
console.log(typeof value2);

console.log(value);

// String
// Number
// Boolean
// undefined
// function



function two() {
    return function () {
        console.log('two');
    }
}

let myFunction2 = two();
myFunction2();

function three() {
    return function() {
        return 'three';
    }
}
console.log(three()())