const permute = (nums) => {
    const results = [];
    let i = 1;
    const backtrack = (nums, temp) => {
      if (temp.length === nums.length) {
          if(i === 1000000)results.push(temp.slice());
          i++;
        return;
      }
      
      nums.forEach(function(num) {
        if (!temp.includes(num)) {
          temp.push(num);
          backtrack(nums, temp);
          temp.pop();
        }
      });
    };
    
    backtrack(nums, []);
    return results;
  };

console.log(permute([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]));