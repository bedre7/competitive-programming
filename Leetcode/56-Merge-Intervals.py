class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for start, end in intervals:
            if merged and merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
                
        return merged