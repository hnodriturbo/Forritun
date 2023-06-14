// 2 listar til að bera saman

listi1 = []
listi2 = []
nyrlisti = []

// Nota for lúppu og set 100 random tölur milli 0 og 100 inn í listann
for (i=0;i<100;i++) {
    let randomkommutala = Math.random();
    let randomTala = Math.floor(randomkommutala * 100) + 1;
    listi1.push(randomTala);
}
console.log(listi1.join(','));

for (i=0;i<100;i++) {
    //   - breyta -   - Skipun1 -  skipun2 -     - talan -
    let randomTala2 = Math.floor(Math.random() * (101 - 0));
    listi2.push(randomTala2);
}
// .join(' ') sameinar allt innan listi2 í einn streng með . á milli
console.log(listi2.join('.'));

let endatala = 2
let endatalastrengur = endatala.toString();
function eins(listi1,listi2) {
    for (i=0; i < listi1.length; i++) {
        let tala = listi1[i].toString();
        if (tala.endsWith(endatala)) {
            nyrlisti.push(listi1[i]);
        }
    }
    for (i=0; i < listi2.length; i++) {
        let tala = listi2[i].toString();
        if (tala.endsWith(endatala)) {
            nyrlisti.push(listi2[i]);
        }
    }
}
eins(listi1,listi2)
console.log(nyrlisti);



// Þetta kallast object og svipar til dictionary í python.
let students = [
    {
        name: "John",
        grades: {
            math: 90,
            science: 85,
            english: 92,
            history: 88,
            geography: 90
        }
    },
    {
        name: "Alice",
        grades: {
          math: 95,
          science: 88,
          english: 91,
          history: 87,
          geography: 92
        }
    },
    {
        name: "Michael",
        grades: {
          math: 87,
          science: 92,
          english: 83,
          history: 90,
          geography: 91
        }
    },
    {
        name: "Emily",
        grades: {
          math: 93,
          science: 89,
          english: 94,
          history: 85,
          geography: 87
        }
    },
    {
        name: "David",
        grades: {
          math: 91,
          science: 84,
          english: 88,
          history: 92,
          geography: 89
        }
    }
];

// for lúppa sem sækir allt math einkunnir og reiknar út meðaleinkunn
function medaleinkun(students) {
    let medaleinkunn = 0;
    let summa = 0;
    let einkunn = 0;
    
    for (i=0; i < students.length; i++) {
        let student = students[i];
        einkunn = student.grades.math;
        summa += einkunn;
    }

    medaleinkunn = summa / students.length;
    return medaleinkunn;
}

let medaleinkunnn = medaleinkun(students);

console.log('Meðaleinkunn í stærðfræði er: ' + medaleinkunnn);


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
function getAccountInfo(customer) {
    console.log("Name: " + customer.name);
    console.log("Account number: " + customer.account.accountNumber); 
    console.log("Balance: " + customer.account.balance);
}





// Example usage: Accessing customer information
console.log(customers[0].name); // Output: John
console.log(customers[2].account.accountNumber); // Output: AC003
console.log(customers[4].account.balance); // Output: 1500
console.log(getAccountInfo(customers[1]))