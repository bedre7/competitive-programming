from collections import defaultdict
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = defaultdict(int)
        
        count = 0
        for meal in deliciousness:
            for power in range(22):
                count += freq[2 ** power - meal]
            
            freq[meal] += 1
                
        return count % 1_000_000_007