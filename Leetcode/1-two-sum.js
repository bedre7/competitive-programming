//Using HashMaps - Fast! ~O(n)
const twoSum1 = function(nums, target){
    let myMap = new Map();
    for(let i = 0; i < nums.length; i++)
    {
        if(myMap.has(target - nums[i]))
            return [myMap.get(target - nums[i]), i]
        myMap.set(nums[i], i);
    }
}

//Using Brute-Force - slow O(n2)
var twoSum2 = function(nums, target) {
    for(let i = 0; i < nums.length; i++)
    {
        for(let j = i + 1; j < nums.length; j++)
        {
            if(nums[i] + nums[j] === target)
                return [i, j];
        }
    }
    return [];
};

console.log(twoSum2([3, 3], 6));