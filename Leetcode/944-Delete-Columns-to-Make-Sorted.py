class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        toDelete = 0
        
        for i in range(len(strs[0])):
            currLetter = strs[0][i]
            for word in strs:
                if currLetter > word[i]:
                    toDelete += 1
                    break
                currLetter = word[i]
        
        return toDelete