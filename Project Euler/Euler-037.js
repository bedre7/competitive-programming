const isPrime = (num) => {
    if(num == 1) return false;
    for(let divisor = 2; divisor <= Math.sqrt(num); divisor++)
    {
        if(num % divisor == 0) return false;
    }
    return true;
} 

const isTruncatable = (num, firstCall = true) => {
    let temp = num;
    while(num.length >= 1 && isPrime(Number(num)))
        num = (firstCall) ? num.slice(1) : num.slice(0, num.length - 1);
    
    if(num.length == 0 && firstCall)
        return isTruncatable(temp, false);
    return num.length == 0;
}

const truncatableSum = function(){
    let truncatableSum = 0;
    let count = 0;
    for(let num = 11; ;num++)
    {
        if(isTruncatable(String(num)))
        {
            truncatableSum += num;
            count++;
        }
        if(count == 11) return truncatableSum; 
    }
}
console.log(truncatableSum());