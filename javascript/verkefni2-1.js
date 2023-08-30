//-- Hreiðar Pétursson --//
//------- Verkefni ------//

//--- Function sem prentar út alla ---/
function prentaNemendur(students) {
    for (i=0; i < students.length; i++) {
        console.log('Nemandi númer: ' + (i+1))
        console.log('Id: ' + students[i].id);
        console.log('Nafn: ' + students[i].name);
        console.log('Aldur: ' + students[i].age);
        console.log('Bekkur: ' + students[i].grade);
        console.log('');
    }
}
//--- Function sem prentar út alla ---/


//--- Function til að leita eftir ID ---//
function leitaEftirId() {
    // Stimpla inn ID
    function stimplaInnId(callback) {
        rl.question('Sláðu inn ID til að leita að því', (leitarId) => {
            if (/^[A-Z]\d{6}$/.test(leitarId)) {
                callback(leitarId);
            } else {
                console.log('Villa: ID verður að vera Einn bókstafur og sex tölustafir');
                viltuLeitaAftur();
            }
        })
    }
    // Spyrja um að leita aftur
    function viltuLeitaAftur() {
        rl.question('Viltu leita aftur? 1. Já - 2. Nei', (svarLeitaAftur) => {
            if (svarLeitaAftur === '1') {
                keyraLeitaEftirId();
            } else if (svarLeitaAftur === '2') {
                keyravalmynd();
            } else {
                console.log('Ekki rétt valið');
                viltuLeitaAftur();
            }
        });
    }
    // Leitar functionið
    function leita(leitarId) {
        let foundStudent = false;
        for (i = 0; i < students.length; i++) {           
            let student = students[i]
            if (student.id === leitarId) {
                console.log('Ég fann nemandann:');
                console.log('Id: ' + student.id);
                console.log('Nafn: ' + student.name);
                console.log('Aldur: ' + student.age);
                console.log('Bekkur: ' + student.grade);
                console.log('');
                foundStudent = true;
                viltuLeitaAftur();
            }
        } 
        if (!foundStudent) {
            console.log('Enginn nemandi fannst með þetta ID.');
            viltuLeitaAftur();           
        }        
    }
    // Keyra leita eftir ID
    function keyraLeitaEftirId() {
        stimplaInnId((leitarId) => {
            leita(leitarId);
        });
    }
    // Keyri leitina
    keyraLeitaEftirId();
}
//--- ^^ Function til að leita eftir ID ^^ ---//



//--- Function til að leita eftir nafni ---//
function leitaEftirNafni() {
    // Function sem spyr um nafnið og skilar því
    function stimplaInnNafn (callback) {
        rl.question('Sláðu inn nafn til að leita: ', (nafn) => {
            callback(nafn);
        })
    }
    // Function sem leitar //
    function leita(nafn) {      
        for (i=0; i < students.length; i++) {
            let fannNemanda = false;
            let nemandi = students[i];
            if (nemandi.name === nafn) {
                console.log(`Fann nemanda með nafnið ${nafn}`)
                console.log('-----------------')
                console.log('Id: ' + nemandi.id);
                console.log('Nafn: ' + nemandi.name);
                console.log('Aldur: ' + nemandi.age);
                console.log('Bekkur: ' + nemandi.grade);
                console.log('');
                fannNemanda = true;
                break;
            }
        }
        if (fannNemanda === false) {
            console.log('Nemandi fannst ekki');
        }
        viltuLeitaAftur();
    }
    // Viltu leita aftur //
    function viltuLeitaAftur() {
        rl.question('Viltu leita aftur? 1. Já - 2. Nei :: ', (val) => {
            if (val === '1') {
                leitaEftirNafni();
            } else if (val === '2') {
                keyravalmynd();
            } else {
                console.log(`${val} er ekki rétt valið. Reyndu aftur`)
                viltuLeitaAftur();
            }
        })
    }
    // Function sem keyrir leitaeftirnafni
    function keyraLeitaEftirNafni() {
        stimplaInnNafn((nafn) => {
            leita(nafn);
        })
    }
    keyraLeitaEftirNafni();
}
//--- ^^ Function til að leita eftir nafni ^^ ---//

// --- Function sem býður að uppfæra nemanda --- //
function uppfaeraNemanda(students) {
    function veljaNemanda(callback) {
        prentaNemendur(students);
        rl.question('Hvaða nemanda viltu uppfæra? ', (indexNemanda) => {
            let numerNemanda = parseInt(indexNemanda) - 1;
            if(numerNemanda >= 0 && numerNemanda <= students.length) {
                let nemandi = students[numerNemanda];
                callback(nemandi, numerNemanda);
            } else {
                console.log(`${indexNemanda} er ekki rétt valið`);
                veljaNemanda(callback);
            }
        })
    }
    function veljaEiginleika(nemandi, callback) {
        console.log('ID: ' + nemandi.id);
        console.log('Nafn: ' + nemandi.name);
        console.log('Aldur: ' + nemandi.age);
        console.log('Bekkur: ' + nemandi.grade);
        rl.question('Hvaða eiginleika viltu uppfæra? 1. Id - 2. Nafn - 3. Aldur - 4. Bekkur', (val) => {
            let eiginleiki;
            switch (val) {
                case '1':
                    eiginleiki = 'id';
                    callback(eiginleiki);
                    break;
                case '2':
                    eiginleiki = 'name';
                    callback(eiginleiki);
                    break;
                case '3':
                    eiginleiki = 'age';
                    callback(eiginleiki);
                    break;
                case '4':
                    eiginleiki = 'grade'
                    callback(eiginleiki);
                    break;
                default:
                    console.log(`${val} er rangt valið. Reyndu aftur`)
                    veljaEiginleika(nemandi, callback);
                    return;
            }

        })
    }

    function uppfaera(students, numerNemanda, eiginleiki, callback) {
        rl.question(`Í hvað viltu breyta ${eiginleiki} ?`, (nyttGildi) => {
            students[numerNemanda][eiginleiki] = nyttGildi;
            callback(nyttGildi, eiginleiki);
        })
        
    }
    function buidAdBreyta(nyttGildi, eiginleiki) {
        console.log(`Það tókst að breyta ${eiginleiki} í ${nyttGildi}`);
        viltuHaldaAfram();
    }
    function viltuHaldaAfram() {
        rl.question('Viltu halda áfram að breyta? 1. Já - 2. Nei', (valHaldaAfram) => {
            if (valHaldaAfram === '1') {
                uppfaeraNemanda(students);
            } else if (valHaldaAfram === '2') {
                keyravalmynd();
            } else {
                console.log(`${valHaldaAfram} er vitlaust valið. Reyndu aftur`);
                viltuHaldaAfram();
            }
        })
    }
    function keyraBreytaGildi() {
        veljaNemanda((nemandi,numerNemanda) => {
            veljaEiginleika(nemandi, (eiginleiki) => {
                uppfaera(students, numerNemanda, eiginleiki, (nyttGildi) => {
                    buidAdBreyta(nyttGildi, eiginleiki);
                });
                
            })
        })
    }
    keyraBreytaGildi();

}






//-------------- Menu --------------//
// Opna readline
const readline = require('readline');
// Opna readline ^^

// Bý til interface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// Bý til interface ^^

// Function sem prentar út valmyndina
function valmynd() {
    console.log('--- Velkominn ---');
    console.log('1. Bæta við Nemanda');
    console.log('2. Leita eftir ID');
    console.log('3. Leita eftir nafni');
    console.log('4. Uppfæra nemanda');
    console.log('5. Eyða nemanda');
    console.log('6. Sýna allann listann')
    console.log('7. Hætta');
    console.log('-----------------');
}
// Function sem prentar út valmyndina ^^

// Function sem keyrir kóða út frá input
function hondlainput(val) {
    switch (val) {
        case '1':
            break;
        case '2':
            leitaEftirId();
            break;
        case '3':
            leitaEftirNafni();
            break;
        case '4':
            uppfaeraNemanda(students);
            break;
        case '5':
            break;
        case '6':
            prentaNemendur(students);
            keyravalmynd();
            break;
        case '7':
            rl.close();
            break;
        default:
            console.log(`${val} er ekki rétt valið.`);
            console.log('Vinsamlegast veldu rétt');
            keyravalmynd();
            break;
    }
}
// Function sem keyrir kóða út frá input ^^

// Functionið sem keyrir valmyndina
function keyravalmynd() {
    valmynd();
    rl.question('Vinsamlegast veldu: ', (val) => {
        hondlainput(val);
    })
}
// Keyri valmyndina
keyravalmynd();
// Functionið sem keyrir valmyndina ^^
//------------ ^^ Menu ^^ ------------//




//--- Array sem geymir öll nemenda object ---//
const students = [
    {
      id: 'A123456',
      name: 'John Smith',
      age: 18,
      grade: '12th'
    },
    {
      id: 'A546856',
      name: 'Emma Johnson',
      age: 17,
      grade: '11th'
    },
    {
      id: 'A325826',
      name: 'Michael Brown',
      age: 16,
      grade: '10th'
    },
    {
      id: 'A851286',
      name: 'Sophia Davis',
      age: 17,
      grade: '11th'
    },
    {
      id: 'A189456',
      name: 'Daniel Wilson',
      age: 16,
      grade: '10th'
    },
    {
      id: 'A854612',
      name: 'Olivia Anderson',
      age: 15,
      grade: '9th'
    },
    {
      id: 'A495723',
      name: 'James Thomas',
      age: 18,
      grade: '12th'
    },
    {
      id: 'A491568',
      name: 'Emily Martin',
      age: 16,
      grade: '10th'
    },
    {
      id: 'A792597',
      name: 'William Garcia',
      age: 17,
      grade: '11th'
    },
    {
      id: 'A581692',
      name: 'Ava Rodriguez',
      age: 15,
      grade: '9th'
    }
];
//--- ^^ Array sem geymir öll nemenda object ^^ ---//