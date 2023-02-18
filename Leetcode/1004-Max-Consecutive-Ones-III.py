class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        longest = 0
        flips = 0
        
        while right < len(nums):
            if nums[right] == 0:
                flips += 1
                while flips > k:
                    if nums[left] == 0:
                        flips -= 1
                    left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest