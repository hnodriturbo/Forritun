var counter = (function() {
    
    // private stuff
    let count = 0;

    function print(message){
        console.log(`${message} => ${count}`);
    }

    function getCount() { return count; }

    function setCount(value) { count = value; }

    function incrementCount() {
        count += 1;
        print('After increment: ');
    }

    function resetCount() {
        print('Before reset: ');
    }
    // return an object
    return {
        get: getCount,
        set: setCount,
        increment: incrementCount,
        reset: resetCount,
        print: print
    };

})();


counter.set(5);
counter.print('talan fór úr engu yfir í')
console.log(counter.get());
counter.increment();
counter.increment();
console.log(counter.get());