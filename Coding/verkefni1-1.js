
// lítrar í gallon reiknivélin mín
function litrarigallon(litrar) {
    gallon = litrar * 3.25;
    return gallon;
}

fimmlitrar = litrarigallon(5);

console.log(fimmlitrar);


// Hraðatakmörk verkefni
function hversuhratt(hradi) {
    if (hradi < 30) {
        console.log('hraðinn er minni en 30km klst');
    }
    else if (hradi > 30) {
        mismunur = hradi - 30;
        hversuoftfimmyfir = mismunur / 5;
        refstistig = hversuoftfimmyfir * 3;
        roundednidurstada = Math.ceil(refstistig);
        console.log('þú ert með: ' + roundednidurstada + ' refsistig');
    }   
}


hversuhratt(56)
// Tala og veldi verkefni
function talaveldi(tala,veldi) {
    let summa = Math.pow(tala,veldi)
    let equation = "";
    for (let i=0; i<veldi; i++) {
        equation += tala.toString();
        if (i < veldi - 1) {
            equation += " * ";
        }
    }
    console.log(equation + " = " + summa);
}

talaveldi(5,10)

const readline = require('readline');
// Bý til interface til að fá input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// Teningakast
function kasta(oft) {
    let summa = 0
    for (i=0;i<oft;i++) {
        // bý til random kommutölu milli 0 og 1
        let randomDecimal = Math.random();
        // Geri kommutöluna í random tölu milli 1 og 6
        let randomNumber = Math.floor(randomDecimal * 6) + 1;
        
        // Bæti tölunni við summuna
        summa += randomNumber
    }
    return summa;
}

rl.question('Sláðu inn hversu oft skal kasta: ', (oft) => {
    const sum = kasta(Number(oft));
    console.log(sum + ' er summan af ' + oft + ' köstum');
    rl.close();
})

