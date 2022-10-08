const longestCommonPrefix = function(strs)
{
    let commonPrefix = '';

    for(let i = 0; i < strs[0].length; i++)
    {
        let temp = strs[0][i];
        for(let j = 0; j < strs.length; j++)
        {
           if(strs[j][i] !== temp)
                return commonPrefix;
        }
        commonPrefix += temp;
    }
    return commonPrefix;
}

console.log(longestCommonPrefix(["dog","racecar","car"]));