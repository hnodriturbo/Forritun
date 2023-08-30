// HREIÐAR PÉTURSSON
// VERKEFNI UNNIÐ 14-16 JÚNÍ 2023
// BANKAREIKNINGAR VERKEFNI


/*--- OPNA READLINE OG BÝ TIL INTERFACE ---*/
// krefst readline -- svipað import
const readline = require('readline');

// Bý til interface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
/*--- OPNA READLINE OG BÝ TIL INTERFACE ---*/



/*--- FUNCTION SEM PRENTAR ÚT MENU VALMYNDINA ---*/
function menu() {
    console.log('--- Velkomin í bankann minn ---');
    console.log('1. Prenta út alla reikninga');
    console.log('2. Leggja inn pening');
    console.log('3. Taka út pening');
    console.log('4. Eyða viðkomandi');
    console.log('5. Samanlögð innistæðan í bankanum');
    console.log('6. Hæðsta innistæðan í bankanum');
    console.log('7. Hætta');
}
/*--- FUNCTION SEM PRENTAR ÚT MENU VALMYNDINA ---*/



/*--- FUNCTION SEM ÁKVEÐUR HVAÐ ER GERT VIÐ ÞAÐ SEM ER SLEGIÐ INN (VAL) ---*/
function hondlainput(val) {
    switch (val) {
        case '1': // Prenta út alla viðskiptavini
            prentaAccounts(customers);
            promptaUser();
            break;
        case '2': // Innlögn
            innlogn();
            break;
        case '3': // Úttekt
            takaut();
            break;
        case '4': // Eyða viðskiptavin
            eydavidskiptavin();
            break;           
        case '5': // Samanlögð innistæða allra reikninga
            samanlogdinnistaeda(customers);
            break;
        case '6': // Hæðsta innistæðan í bankanum
            haedstainnistaedan(customers);
            break;
        default:
            console.log('Valdir ekki rétt, reyndu aftur');
            promptaUser();
            break;
    }
}
/*--- FUNCTION SEM ÁKVEÐUR HVAÐ ER GERT VIÐ ÞAÐ SEM ER SLEGIÐ INN (VAL) ---*/



/*--- FALLIÐ SEM KEYRIR FORRITIÐ ---*/
// Function sem promptar upp spurningu og setur valið í breytu
function promptaUser() {
    menu()
    rl.question('Vinsamlega veldu: ', (val) => {
        if (val === '7') {
            rl.close();
        } else {
            hondlainput(val);    
        }
    });
}
promptaUser();
/*--- FALLIÐ SEM KEYRIR FORRITIÐ ---*/






/* ------------------------------------------------------ */
/* --- MENUIÐ ER FYRIR OFAN OG FUNCTIONS FYRIR NEÐAN ---- */
/* ------------------------------------------------------ */





/*--- HÉR KOMA ÖLL FUNCTION FORRITSINS ---*/





//----- PRENTA ALLA ACCOUNTS -----//
function prentaAccounts(customers) {
    for (i=0; i < customers.length; i++) {
        console.log('Númer viðskiptavins: ' + (i+1))
        console.log('Name: ' + customers[i].name)
        console.log('Account number: ' + customers[i].account.accountNumber)
        console.log('Staðan á reikningnum: ' + customers[i].account.balance)
    }
}
//----- PRENTA ALLA ACCOUNTS -----//



//----- FUNCTION FYRIR INNLÖGN -----//
function innlogn() {
    prentaAccounts(customers); // Sýni alla accounta
    rl.question('Veldu hvaða viðskiptavin þú vilt leggja inn á: ', (numervidskiptavins) => {
        let valinnvidskiptavinur = customers[numervidskiptavins - 1];
        rl.question(`Hvað viltu leggja mikið inná ${valinnvidskiptavinur.name}`, (upphaed) => {
            // upphaedInt = parseInt(upphaed)
            // upphaedFloat = parseFloat(upphaed)
            // upphaedStrengur = upphaed.toString()
            upphaedInt = parseInt(upphaed);
            valinnvidskiptavinur.account.balance += upphaedInt;
            console.log(`Búið að leggja inn ${upphaedInt} og staðan á reikningnum er núna: ${valinnvidskiptavinur.account.balance}`);
            promptaUser();
        })
    })
}
//----- FUNCTION FYRIR INNLÖGN -----//



//----- FUNCTION FYRIR ÚTTEKT -----//
function takaut() {
    function veljavidskiptavin(callback) {
        rl.question('Veldu hvaða viðskiptavin þú vilt taka út af: ' , (numervidskiptavins) => {
            let valinnvidskiptavinur = customers[numervidskiptavins - 1];
            callback(valinnvidskiptavinur);
        });
    }    
    function uttekt() {
        prentaAccounts(customers);
        veljavidskiptavin((valinnvidskiptavinur) => {
            console.log(`þú valdir ${valinnvidskiptavinur.name}`);
            adaluttekt(valinnvidskiptavinur);
        });   
    }   
    function adaluttekt(valinnvidskiptavinur) {
        rl.question(`Hvað viltu taka mikið út? (${valinnvidskiptavinur.account.balance} er í boði)`, (upphaed) => {          
            upphaedInt = parseInt(upphaed);
            if (upphaedInt <= valinnvidskiptavinur.account.balance) {
                valinnvidskiptavinur.account.balance -= upphaedInt;
                console.log(`Búið að taka út ${upphaedInt} og staðan er ${valinnvidskiptavinur.account.balance}`)
                promptaUser();
            } else {
                console.log(`${upphaedInt} er meira en er inná reikning og því ekki hægt að taka það út`)
                adaluttekt(valinnvidskiptavinur);
            }
        });
    }
    uttekt();
}
//----- FUNCTION FYRIR ÚTTEKT -----//



//----- FUNCTION TIL AÐ EYÐA -----//
function eydavidskiptavin() {
    // Skilgreini index viðskiptavins sem 0
    let indexvidskiptavins = 0;
    // Function sem skilar völdum viðskiptavin og indexi hans með callback
    function veljaviskiptavin(callback) {        
        rl.question('Veldu hvaða viðskiptavin þú vilt eyða', (numervidskiptavins) => {
            indexvidskiptavins = numervidskiptavins - 1;
            let valinnvidskiptavinur = customers[indexvidskiptavins];
            callback(valinnvidskiptavinur, indexvidskiptavins);
        });
    }
    // Ef svarið er já(1) þá notast ég við splice til að eyða viðkomandi út frá indexi valins viðskiptavins
    function ertuviss(valinnvidskiptavinur, indexvidskiptavins) {
        rl.question(`Ertu viss þú viljir eyða ${valinnvidskiptavinur.name} út úr kerfinu?
                    1 = Já --- 2 = Hætta við`, (svar) => {
           if (svar === '1') {
            customers.splice(indexvidskiptavins, 1);
            console.log(`${valinnvidskiptavinur.name} hefur verið eytt úr skránni`);
            promptaUser();
           } else if (svar === '2') { // ef svarið er nei þá sendi ég viðkomandi til baka í menu
            promptaUser();
           } else { // Ef vitlaust er valið færðu villuskilaboð og ert sendur tilbaka í ertuviss function
            console.log('Verður að velja 1 eða 2');
            ertuviss(valinnvidskiptavinur, indexvidskiptavins);
           }
        });
    }
    // Function sem keyrir öll function sem ég bjó til að eyða viðskiptavin út
    function eyda() {
        // Prenta út alla accounta
        prentaAccounts(customers);
        // Keyri veljaviskiptavin og innan í því keyri ég ertuviss sem eyðir út viðkomandi
        veljaviskiptavin((valinnvidskiptavinur) => {
            console.log(`Þú valdir ${valinnvidskiptavinur.name}`);
            ertuviss(valinnvidskiptavinur, indexvidskiptavins);
        });
    }

    eyda();
}
//----- FUNCTION TIL AÐ EYÐA -----//



//----- FINNA ÚT SUMMU ALLRA INNISTÆÐNA -----//
function samanlogdinnistaeda(customers) {
    let summa = 0;
    for (i=0; i < customers.length; i++) {
        let customer = customers[i];
        summa += customer.account.balance;
    }
    console.log('Summa allra reikninga er: ' + summa);
    promptaUser();
}
//----- FINNA ÚT SUMMU ALLRA INNISTÆÐNA -----//



//----- FINNA HÆÐSTU INNISTÆÐUNA -----//
function haedstainnistaedan(customers) {
    let haedstainnistaeda = -Infinity;
    let customermedhaedstuinnistaeduna = null;

    for (i=0; i < customers.length; i++) {
        let customer = customers[i];
        let customerbalance = customer.account.balance;

        if (customerbalance > haedstainnistaeda) {
            haedstainnistaeda = customerbalance;
            customermedhaedstuinnistaeduna = customer;
        }
    }

    console.log('Viðskiptavinurinn með hæðstu innistæðuna er: ');
    console.log(customermedhaedstuinnistaeduna.name);
    console.log(customermedhaedstuinnistaeduna.account);
    promptaUser();
}
//----- FINNA HÆÐSTU INNISTÆÐUNA -----//





/*--- Array sem heldur utan um alla einstaklingana ---*/
let customers = [
    {
      name: "John",
      account: {
        accountNumber: "AC001",
        balance: 1000
      }
    },
    {
      name: "Jane",
      account: {
        accountNumber: "AC002",
        balance: 2500
      }
    },
    {
      name: "Mike",
      account: {
        accountNumber: "AC003",
        balance: 500
      }
    },
    {
      name: "Emily",
      account: {
        accountNumber: "AC004",
        balance: 3000
      }
    },
    {
      name: "Michael",
      account: {
        accountNumber: "AC005",
        balance: 1500
      }
    }

  ];
