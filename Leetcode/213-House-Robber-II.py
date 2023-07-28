class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        # [9, 7, 0, 300, 1]
        # [9, 307, 1, 300, 1]
        def dp(houses, start, end):
            maxMoney = houses[end]
            for i in range(end - 2, start - 1, -1):
                currMax = maxMoney
                houses[i] += maxMoney
                maxMoney = max(maxMoney, houses[i + 1])
            
            maxMoney = max(maxMoney, houses[start])
            return maxMoney
        
        return max(dp(nums.copy(), 0, len(nums) - 2), dp(nums.copy(), 1, len(nums) - 1))