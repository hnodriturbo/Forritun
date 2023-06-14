/*
for (i = 0; i < 10; i++) {
    console.log(i);
}
// Keyri for lúppu
//Stilli i sem 0, keyra lúppu á meðan i er minni en 10, hækka i um einn
// í hvert skipti sem lúppan keyrist
for (i = 0; i < 10; i++) {
    console.log(i);
}
*/
/*
let a = [4, 8, 15, 16, 23, 42];
// Skilgreini for lúppu fyrst, svo opna bracket sem keyrir kóðann sem
// á að keyrast í hvert skipti sem lúppan keyrir

// lúppan keyrir jafnoft og lengd a er -- hækka i um einn í hvert skipti
for (i = 0; i < a.length; i++) { 
    console.log(a[i]);
}

for (i = 0; i < a.length; i++) { 
    console.log(a[i]);
    console.log(a)
    console.log('bil');
}
array = 0
for (let index = 0; index < array.length; index++) {
    const element = array[index];
}

for (let b = 0; b < a.length; b++) {
    const c = a[b];
    console.log(c);
    
}
*/



let x = 1;
while (x < 10) {
    console.log(x++);
    
    if (x == 7) break;
    /*
    if (x == 7) {
        break;
    }
    */

}

while (true) {
    console.log('prufa');
    break
}