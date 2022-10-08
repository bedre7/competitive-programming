'use strict'

const findABC = function(){
    for(let a = 1; a < 1000; a++)
    {
        for(let b = 1; b < 1000; b++)
        {
            if(a + b + Math.sqrt(a ** 2 + b ** 2) === 1000)
                return a * b * Math.sqrt(a ** 2 + b ** 2);
        }
    }
}

console.log(findABC());