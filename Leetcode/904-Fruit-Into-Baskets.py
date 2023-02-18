from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxCount = 0
        l = 0
        basket = defaultdict(int)
        
        for fruit in fruits:
            if len(basket.keys()) == 2 and fruit not in basket:
                while len(basket.keys()) > 1:
                    basket[fruits[l]] -= 1
                    if basket[fruits[l]] == 0:
                        del basket[fruits[l]]
                    l += 1
                    
            basket[fruit] += 1
            maxCount = max(maxCount, sum(basket.values()))
        
        return maxCount