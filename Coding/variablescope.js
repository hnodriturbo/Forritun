let a = 'first';

// b er ekki til nema inn í function
function scopeTest() {
    console.log(a);

    let b = 'second'
    // c verður ekki til
    if (a != 'eitthvað annað') {
        console.log(a);
        console.log('inside if: ' + b);

        // let c = 'third';
    }
    // console.log(c);
   // let b = 'second';
}

scopeTest();
// console.log(b);
