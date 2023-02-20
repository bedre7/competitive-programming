from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occur = defaultdict(int)
        left = right = 0
        longest = 0
        
        while right < len(s):
            while occur[s[right]] > 0:
                occur[s[left]] -= 1
                left += 1
            occur[s[right]] += 1
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest