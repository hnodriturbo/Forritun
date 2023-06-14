// krefst readline -- svipað import
const readline = require('readline');

// Bý til interface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function sem sýnir display menu
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
function hondlainput(val) {
    switch (val) {
        case '1':
            // hérna kemur function númer 1
            break;
        case '2':
            // hérna kemur function númer 2
            break;
        case '3':
            // hérna kemur function númer 3
            break;
        case '4':
            // hérna kemur function númer 4
            break;
        case '5':
            // hérna kemur function númer 5
            break;
        case '6':
            // Hætta valmöguleikinn
            rl.close();
            break;
        default:
            console.log('Valdir ekki rétt, reyndu aftur');
            break;
                            
    }
}

// Function sem promptar upp spurningu og keyrir
function promptaUser() {
    menu()
    rl.question('Vinsamlega veldu: ', (val) => {
        hondlainput(val);
        promptaUser();
    })
}

promptaUser();