
const terms = new Set([]);
for(let i = 2; i <= 100; i++)
{
    for(let j = 2; j <= 100; j++)
    {
        terms.add(i ** j);
    }
}
const termsArr = Array.from(terms);
console.log(termsArr.length);