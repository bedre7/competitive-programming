from collections import defaultdict

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = defaultdict(int)
        
        for char in words[0]:
            count[char] += 1
            
        for char in count.keys():
            for word in words[1:]:
                count[char] = min(count[char], word.count(char))
        
        result = []
        for char in count.keys():
            if count[char] != 0:
                result += [char] * count[char]
        
        return result