class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spacedStr = []
        
        i = j = 0
        while i < len(s):
            if j < len(spaces) and spaces[j] == i:
                spacedStr.append(' ')
                j += 1
            else:
                spacedStr.append(s[i])
                i += 1
        
        return ''.join(spacedStr)