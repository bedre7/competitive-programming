from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowMap = defaultdict(int)
        
        for i in range(len(grid)):
            rowMap[str(grid[i])] += 1
        
        count = 0
        for i in range(len(grid[0])):
            currCol = []
            for j in range(len(grid)):
                currCol.append(grid[j][i])
            strCol = str(currCol)
            if strCol in rowMap:
                count += rowMap[strCol]
        
        return count