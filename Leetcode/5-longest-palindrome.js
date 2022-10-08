'use strict'

const s = 'babad';

const isPalindrome = (str) => str === str.split('').reverse().join('');

const longestPalindrome = function(s)
{
    let longestPali = s[0];
    let temp = '';

    if(isPalindrome(s)) return s;

    let str = '';

    for(let i = 0; i < s.length; i++)
    {
        str = s[i];
        for(let j = i + 1; j < s.length; j++)
        {
            str += s[j];
            temp += s[j];
            if(isPalindrome(str))
            {
                if(str.length > longestPali.length)
                {
                    longestPali = temp = str;
                }
                str = '';
            }
            if(isPalindrome(temp))
            {
                if(temp.length > longestPali.length)
                    longestPali = temp;
            }
        }
    }
    return longestPali;
}
console.log(longestPalindrome('abb'));
