class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = len(piles)
        picks = coins // 3
        
        myCoins = 0
        piles = piles[coins//3:]
        
        for _ in range(picks):
            piles.pop()
            myCoins += piles.pop()
        
        return myCoins