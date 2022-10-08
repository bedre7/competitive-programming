
const devide = function(dividend, divisor) {
    if(Math.abs(dividend) === Math.abs(divisor)) 
        return dividend !== divisor ? -1 : 1;  
    
    if(dividend < divisor) return 0;
    
    let quotient = Math.round(Math.pow(10, (Math.log10(Math.abs(dividend)) 
            - Math.log10(Math.abs(divisor)))));
    if(dividend * divisor < 0) quotient *= -1;
    
    return (quotient > (2147483647)) ? 2147483647 : 
    quotient < (-2147483648) ? (-2147483648) : quotient;
}

console.log(devide(2147483647, 1));
console.log(devide(11, -2));

// while(Math.abs(dividend) >= Math.abs(divisor))
    // {
    //     (dividend * divisor < 0) ? quotient-- : quotient++;
    //     dividend > 0 ? dividend -= Math.abs(divisor) : dividend += Math.abs(divisor);
    // }