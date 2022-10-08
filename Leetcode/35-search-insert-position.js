const searchInsert = function(nums, target) {
    
    let index = 0;
    while(nums.length !== 0)
    {
        let start = 0, last = nums.length - 1;
        middleIndex = Math.trunc((start + last) / 2);
        
        if(target > nums[middleIndex]){
             nums.splice(start, middleIndex + 1);
             start = middleIndex + 1;
             index += start;
        }
        else if(target < nums[middleIndex])
        {
            nums.splice(middleIndex);
            last = middleIndex - 1;
        }
        else return Math.trunc(index + last / 2);
    }

    return index;
};

console.log(searchInsert([6,7,8], 7));