class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = count = maxVowels = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
                maxVowels = max(maxVowels, count)
            if r - l + 1 == k:
                if s[l] in vowels:
                    count -= 1
                l += 1
        
        return maxVowels