
const generateTrigNumber = function(nth)
{
    let value = 0;
    for(let i = 1; i <= nth; i++)
        value += i;
    return value;
}

const countDivisors = function(number)
{
    let count = 0;
    for(let i = 1; i <= Math.sqrt(number); i++)
        if(number % i === 0) 
        {
            count += (i === number / i) ? 1: 2;
        }
    return count;
}
const findTrigNumber = function()
{
    for(let i = 1; ;i++)
    {
        const currentNum = generateTrigNumber(i);
        const count = countDivisors(currentNum);
        console.log(count, currentNum);
        if(count > 500) return currentNum;
    }
}
console.log(findTrigNumber());