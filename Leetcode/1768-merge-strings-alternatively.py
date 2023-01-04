class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        size1 = len(word1)
        size2 = len(word2)
        
        left = right = 0
        
        while left < size1 or right < size2:
            if left < size1:
                merged += word1[left]
                left += 1
            if right < size2:
                merged += word2[right]
                right += 1
        
        return merged
            