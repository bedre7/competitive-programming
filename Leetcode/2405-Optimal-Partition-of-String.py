class Solution:
    def partitionString(self, s: str) -> int:
        partitions = []
        
        currCounter = {}
        start = 0
        for i, c in enumerate(s):
            if c in currCounter:
                partitions.append(s[start:i])
                currCounter.clear()
                start = i
                currCounter[c] = 1
            else:
                currCounter[c] = 1
                
        partitions.append(s[start:])
        
        return len(partitions)