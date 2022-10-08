const symbols = new Map([
    ['I', 1],
    ['V', 5],
    ['X', 10],
    ['L', 50],
    ['C', 100],
    ['D', 500],
    ['M', 1000]
]);

const specials = new Map([
    ['IV', 4],
    ['IX', 9],
    ['XL', 40],
    ['XC', 90],
    ['CD', 400],
    ['CM', 900]
]);

const romanToInt = function(s)
{
    let num = 0;
    for(let i = 0; i < s.length; i++)
    {
        if(s[i] === 'I' || s[i] === 'X' || s[i] === 'C')
        {     
            if(specials.has(s[i] + s[i + 1]))
            {
                num += specials.get(s[i] + s[++i]);
                continue;
            }
        }
        let digit = symbols.get(s[i]);
        num += digit;
    }
    return num;
}
console.log(romanToInt("MCMXCIV"));