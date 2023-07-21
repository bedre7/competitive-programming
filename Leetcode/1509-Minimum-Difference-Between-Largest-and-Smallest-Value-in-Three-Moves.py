class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        nums.sort()
        #1
        res = nums[-1] - nums[3]
        #2
        res = min(res, nums[-4] - nums[0])
        #3
        res = min(res, nums[-2] - nums[2])
        #4
        res = min(res, nums[-3] - nums[1])
        return res