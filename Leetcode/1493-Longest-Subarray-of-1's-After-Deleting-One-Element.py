class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = longest = zeros = 0
        zeroIndex = None
        
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
                if zeros == 2:
                    zeros -= 1
                    l = zeroIndex + 1
                zeroIndex = r
            longest = max(r - l - zeros + 1, longest)
            
            r += 1
        
        return longest if zeroIndex else longest - 1