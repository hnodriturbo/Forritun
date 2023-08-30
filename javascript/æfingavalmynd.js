const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function valmynd() {
    console.log('Valmyndin mín');
    console.log('1. Eitthvað');
    console.log('2. Hætta');
}

function hondlainput(val) {
    switch (val) {
        case '1':
            break;
        case '2':
            break;
        default:
            console.log('villa, reyndu aftur')
            keyravalmynd();
    }
}

function keyravalmynd() {
    valmynd();
    rl.question('Veldu hvað þú vilt gera', (val) => {
        hondlainput(val);
    })
}
keyravalmynd();