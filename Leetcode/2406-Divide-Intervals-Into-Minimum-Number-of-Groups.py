class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        maxPos = float('-inf')
        for l, r in intervals: maxPos = max(maxPos, l, r)

        prefix = [0] * (maxPos + 1)

        for i in range(len(intervals)):
            l, r = intervals[i]
            prefix[l - 1] += 1
            prefix[r] += -1
        
        for i in range(1, maxPos):
            prefix[i] += prefix[i - 1]
        
        prefix.pop()

        return max(prefix)