const numbers = new Map([
    [1, 'one'],
    [2, 'two'],
    [3, 'three'],
    [4, 'four'],
    [5, 'five'],
    [6, 'six'],
    [7, 'seven'],
    [8, 'eight'],
    [9, 'nine'],
    [10, 'ten'],
    [11, 'eleven'],
    [12, 'twelve'],
    [13, 'thirteen'],
    [14, 'fourteen'],
    [15, 'fifteen'],
    [16, 'sixteen'],
    [17, 'seventeen'],
    [18, 'eighteen'],
    [19, 'nineteen'],
    [20, 'twenty'],
    [30, 'thirty'],
    [40, 'forty'],
    [50, 'fifty'],
    [60, 'sixty'],
    [70, 'seventy'],
    [80, 'eighty'],
    [90, 'ninety'],
    [100, 'hundred'],
    [1000, 'thousand']
])

const countDigitLetters = function()
{
    let count = 0;
    for(let i = 1; i <= 1000; i++)
    {
        const strNum = i + '';
        if(strNum.length === 1)
            count += numbers.get(i).length;
        else if(strNum.length === 2)
        {
            count += countTwoDigit(strNum, i);
        }
        else if(strNum.length === 3)
        {
            if(i % 100 === 0) count += numbers.get(Number(strNum[0])).length + 7;
            else
            {
                const temp = numbers.get(Number(strNum[0])).length + 7 + 3 + countTwoDigit(strNum.slice(1));
                count += temp;
            }
        }
        else count += 11;
    }
    return count;
}
const countTwoDigit = function(strNum, intNum = Number(strNum))
{
    let count = 0;
    
    if(intNum % 10 === 0 || (intNum > 0 && intNum < 20))
        count += numbers.get(intNum).length;
    else
    {   
        count = numbers.get(Number(strNum[0] + '0')).length 
            + numbers.get(Number(strNum[1])).length;
    }
    return count;
}
console.log(countDigitLetters());