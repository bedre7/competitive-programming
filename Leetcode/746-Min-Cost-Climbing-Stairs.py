class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cache = {}
        # def dp(index):
        #     if index >= len(cost):
        #         return 0
        #     if index in cache: return cache[index]
        #     oneStep = dp(index + 1)
        #     twoStep = dp(index + 2)
        #     cache[index] = min(oneStep, twoStep) + cost[index]
        #     return cache[index]
        
        # return min(dp(0), dp(1))
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])