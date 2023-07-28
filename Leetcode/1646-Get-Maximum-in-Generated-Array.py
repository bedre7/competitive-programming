class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 or n == 1: return n
        nums = [0] * (n + 2)
        nums[1] = 1
        maxNum = 0
        for i in range(1, n // 2 + 1):
            if 2 <= 2 * i <= n:
                nums[i * 2] = nums[i]
            if 2 <= 2 * i + 1 <= n:
                nums[i * 2 + 1] = nums[i] + nums[i + 1]
            maxNum = max(maxNum, nums[i * 2], nums[i * 2 + 1])
        
        return maxNum