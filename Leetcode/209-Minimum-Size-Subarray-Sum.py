class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minLen = n
        found = False
        left = 0
        curr = 0
        for right in range(n):
            curr += nums[right]
            while curr >= target:
                found = True
                minLen = min(minLen, right - left + 1)
                curr -= nums[left]
                left += 1
            
        return minLen if found else 0