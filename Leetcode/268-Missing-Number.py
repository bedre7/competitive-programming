class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        currNum = 0
        
        for i in range(len(nums)):
            if nums[i] != currNum:
                return currNum
            currNum += 1
        
        return currNum