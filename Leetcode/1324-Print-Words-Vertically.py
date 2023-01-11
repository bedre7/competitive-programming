class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        output = []
        
        longestWord = max(words, key=len)
        
        for i in range(len(longestWord)):
            currWord = ''
            for j in range(len(words)):
                if i >= len(words[j]):
                    currWord += ' '
                else:
                    currWord += words[j][i]
            currWord = currWord.rstrip()
            output.append(currWord)
            
        return output