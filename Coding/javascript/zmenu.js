// Fyrst importa ég readline
const readline = require('readline');

// Búa til interface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function sem displayar menu
function menu() {
    console.log('--- Velkomin í bankann minn ---')
    console.log('1. Fá upplýsingar um bankareikning viðkomandi')
    console.log('2. Leggja inn pening')
    console.log('3. Taka út pening')
    console.log('4. Eyða viðkomandi')
    console.log('5. Hæðsta innistæðan í bankanum')
    console.log('6. Hætta')
}

// Function sem höndlar input
function notandaval(val){
    switch (val) {
        case '1':
            break;
        case '2':
            break;
        case 3:
            rl.close();
            break;
        default:
            console.log('ekki rétt valið, reyndu aftur')
            break;

    }
}

// Function sem leyfir notanda að slá inn valið
function promptaUppValinu() {
    menu()
    rl.question('Vinsamlegast veldu: ', (val) => {
        notandaval(val);
        promptaUppValinu();
    })
}

// Keyri prógrammið
promptaUppValinu();