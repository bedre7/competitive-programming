class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [[interval[0], i] for i, interval in enumerate(intervals)]
        starts.sort(key=lambda x: x[0])
        output = []
        
        def find(x):
            low = 0
            high = len(starts) - 1
            index = -1
            
            while low <= high:
                mid = (low + high) // 2
                if starts[mid][0] == x: 
                    return starts[mid][1]
                elif starts[mid][0] > x:
                    index = starts[mid][1]
                    high = mid - 1
                else:
                    low = mid + 1
            
            return index

        for start, end in intervals:
            rightInterval = find(end)
            output.append(rightInterval)
        
        return output