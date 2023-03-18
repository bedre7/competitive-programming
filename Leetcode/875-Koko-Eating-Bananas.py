class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def sheCan(perhour, hours):
            time = 0
            for pile in piles:
                time += math.ceil(pile / perhour)
            
            return time <= hours
        
        start = 1
        end = sum(piles)
        k = end
        
        while start <= end:
            mid = (start + end) // 2
            if sheCan(mid, h):
                k = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return k