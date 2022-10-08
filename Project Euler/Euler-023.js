
const isAbundant = function(num){
    let factorsSum = 0;
    for(let i = 1; i <= Math.sqrt(num); i++)
    {
        if(num % i === 0) 
            factorsSum += (i === num / i || i === 1) ? i : i + num / i;   
    }
    return num < factorsSum;
}
const findNonAbundantSum = function()
{
    let sum = 0;
    for(let i = 1; i <= 28123; i++)
        sum += i;
    
     for(let i = 12; i <= 28123; i++)
     {
         for(let j = 12; j <= i / 2; j++)
         {
             if(isAbundant(j) && isAbundant(i - j))
             {
                 sum -= i;
                 break;
             }
         }
     }  
     return sum;
}

console.log(findNonAbundantSum());