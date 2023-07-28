class Solution:
    def rob(self, nums: List[int]) -> int:
        # [9, 7, 0, 300, 1]
        # [9, 307, 1, 300, 1]
        maxMoney = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            currMax = maxMoney
            nums[i] += maxMoney
            maxMoney = max(maxMoney, nums[i + 1])
        
        maxMoney = max(maxMoney, nums[0])
        return maxMoney