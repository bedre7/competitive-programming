from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        occur = Counter(s1)
        window = Counter(s2[:len1])
        
        def areEqual(window, occur):
            for i in range(26):
                if window[chr(i+97)] < occur[chr(i + 97)]:
                    return False
            return True
        
        left = 1
        for right in range(len1, len(s2)):
            if areEqual(window, occur):
                return True
            window[s2[right]] += 1
            window[s2[left - 1]] -= 1
            left += 1
            
        return areEqual(window, occur)