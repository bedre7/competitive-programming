class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = minMax = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            avg = ceil(total / (i + 1))
            minMax = max(minMax, avg)
        return minMax