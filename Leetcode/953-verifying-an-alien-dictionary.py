class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        
        for i in range(len(order)):
            alphabet[order[i]] = i
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                
                if alphabet[words[i][j]] > alphabet[words[i + 1][j]]:
                    return False
                elif alphabet[words[i][j]] < alphabet[words[i + 1][j]]:
                    break
                    
        
        return True