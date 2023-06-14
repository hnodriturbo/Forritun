let a =[4, 8,15, 16, 23, 42];
let b = ['david', 'eddie', 'alex', 'michael']

console.log(a[0]);
console.log(a[1]);
console.log(a[3]);
console.log(a);

a[0] = 7;
console.log(a);

console.log(typeof a);

let c = ['bob',4,'alex', true]
console.log(c);

console.log(b[6]);

console.log(a.length);

a[10] = 'Hreiðar'
console.log(a);
console.log(a.length);

// bæta við listann í enda stakið
a.push('bætti við');
console.log(a);

a.pop(); // eyða síðasta stakinu
console.log(a);

