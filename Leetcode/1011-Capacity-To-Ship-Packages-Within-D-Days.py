class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def shippedInDays(capacity, days):
            dayz = 0
            curr = 0
            for w in weights:
                if curr + w > capacity:
                    dayz += 1
                    curr = 0
                curr += w
            
            return dayz + (1 if curr != 0 else 0)
        
        start = max(weights)
        end = sum(weights)
        best = end

        while start <= end:
            mid = (start + end) // 2
            if shippedInDays(mid, days) <= days:
                best = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return best