const fib = function()
{
    let prev = 1n, cur = 1n, next = 2n;
    for(let i = 3; ;i++)
    {
        next = prev + cur;
        prev = cur;
        cur = next;

        if(String(cur).length === 1000)
            return i;
    }
}

console.log(fib());