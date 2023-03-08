from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        
        left = 0
        occur = defaultdict(int)

        for right in range(len(s)):
            occur[s[right]] += 1
            length = right - left + 1
            if length - max(occur.values()) <= k:
                longest = max(longest, right - left + 1)
            while left <= right and length - max(occur.values()) > k:
                occur[s[left]] -= 1
                left += 1
                length -= 1
                
        return longest