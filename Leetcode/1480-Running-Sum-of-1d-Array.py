class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            output[i + 1] += nums[i] + output[i]
        
        return output[1:]