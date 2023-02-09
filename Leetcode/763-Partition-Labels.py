class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = {}
        for i in range(len(s)):
            occur[s[i]] = i
        
        start = end = 0
        part = 0
        partitions = []
        
        for i, char in enumerate(s):
            end = max(end, occur[char])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        
        return partitions