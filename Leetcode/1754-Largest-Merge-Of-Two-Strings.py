class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        left = right = 0
        
        merged = []
        
        while left < len(word1) and right < len(word2):
            if word1[left:] >= word2[right:]:
                merged.append(word1[left])
                left += 1
            else:
                merged.append(word2[right])
                right += 1
        
        while left < len(word1):
            merged.append(word1[left])
            left += 1
            
        while right < len(word2):
            merged.append(word2[right])
            right += 1
        
        return ''.join(merged)