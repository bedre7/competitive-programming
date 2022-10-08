class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        allWords = s.split(' ')
        filteredWords = list(filter(lambda x: len(x) > 0, allWords))
        return len(filteredWords[-1])