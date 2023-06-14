
// Þetta er ég að prófa mig áfram með random tölur

// Þetta gefur mér random kommutölu milli 0 og 1
console.log(Math.random());

// Fyrst bý ég til random tölu á milli 0 og 1
kommutala = Math.random();
// Svo nota ég Math.floor og margfalda töluna sem ég bjó til með 100. Bæti svo 1 við
randomTala = Math.floor(kommutala * 100) + 1
console.log('fyrsta random talan er: ' + randomTala)
let randomNumer = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
console.log(randomNumer);
let randomNumer2 = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
console.log(randomNumer2);
let randomNumer3 = Math.floor(Math.random() * (100 - 50));
console.log(randomNumer3);

// Prufa mig áfram með random tölur
let randomkommutala = Math.random();
let randomtala = Math.floor(randomkommutala * 100);
console.log('Random talan mín er: ' + randomtala)

function eins(listi1,listi2) {
    for (i=0;i<100;i++) {
        let randomkommutala = Math.random();
        let randomtala = Math.floor(randomkommutala * 100) + 1;
    }
}

