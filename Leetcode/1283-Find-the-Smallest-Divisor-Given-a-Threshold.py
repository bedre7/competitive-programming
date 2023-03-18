class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isValid(divisor):
            total = 0
            for n in nums:
                total += math.ceil(n / divisor)
                if total > threshold: return False
            
            return True
        
        start = 1
        end = max(nums)
        best = end
        
        while start <= end:
            mid = (start + end) // 2
            if isValid(mid):
                best = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return best