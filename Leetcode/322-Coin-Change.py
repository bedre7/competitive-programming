class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        memo = defaultdict(lambda: float("inf"))

        def dfs(coinsLeft, total, count):
            if coinsLeft in memo:
                return memo[coinsLeft] + 1

            if coinsLeft == 0:
                return 1

            for coin in coins:
                if coinsLeft - coin >= 0:
                    memo[coinsLeft] = min(memo[coinsLeft],
                                        dfs(coinsLeft - coin, total + coin, count + 1))
            return memo[coinsLeft] + 1
        
        dfs(amount, 0, 0)
        return memo[amount] if memo[amount] != float("inf") else -1