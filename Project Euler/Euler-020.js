
const factorial = function(num)
{
    let product = 1n, digitSum = 0;
    for(let i = 1n; i <= num; i++)
        product *= i;
    let strNum = (product + '');

    for(let i = 0; i < strNum.length; i++)
        digitSum += Number(strNum[i]);
    return digitSum;
}

console.log(factorial(100));