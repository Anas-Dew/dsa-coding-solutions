/**
 * @param {number} n
 * @return {string[]}
 */

var fizzBuzz = function(n) {
    let fizz = "Fizz";
    let buzz = "Buzz";
    let fb = [];
    for(let i = 1; i <= n; i++) {
        if (i % 5 === 0 && i % 3 === 0) {
            fb.push(fizz+buzz)
        }
        else if(i % 3 === 0){
            fb.push(fizz)
        } else if(i % 5 === 0){
            fb.push(buzz)
        }
        else {
            fb.push(String(i))
        }
    }
    return fb;
};