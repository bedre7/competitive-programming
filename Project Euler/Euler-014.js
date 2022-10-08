
const countMaxChain = function()
{
    let maxCount = 0, maxStarter;
    for(let num = 1000000; num > 0; num--)
    {
        let result = num;
        for(count = 1; result != 1; count++)
        {
            result % 2 === 0 ? result /= 2 : result = 3 * result + 1;
            count++;
        }
        
        if(maxCount < count) 
        {
            maxCount = count;
            maxStarter = num;
        }
    }
    return maxStarter;
}
console.log(countMaxChain());