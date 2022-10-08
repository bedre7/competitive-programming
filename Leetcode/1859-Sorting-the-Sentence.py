class Solution:
    def sortSentence(self, s: str) -> str:
        sortedSentence = s.split(' ')
        sortedSentence.sort(key=lambda x: int(x[-1]))
        return ' '.join([s[:-1] for s in sortedSentence])
