class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxTotal = sum(nums[0:k])
        left = 1
        right = k
        
        window = maxTotal
        while right < n:
            window -= nums[left - 1]
            window += nums[right]
            maxTotal = max(maxTotal, window)
            left += 1
            right += 1
        
        return maxTotal / k