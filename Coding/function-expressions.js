/*
setTimeout(function () {console.log('i waited 2 seconds'); }, 2000);

setTimeout(function () {
    console.log('i waited 2 seconds'); 
}, 2000); // 2000 er millisekúntur sem skal bíða áður en skipun executast
*/
/*
let counter = 0;
function timeout() {
    setTimeout(function () {
        console.log('hi ' + counter++);
        timeout();
    }, 2000)
}

timeout();
*/

(function () {
   console.log('hi');
})(); //auka svigarnir utanum og Loka svigarnir keyra functionið strax

