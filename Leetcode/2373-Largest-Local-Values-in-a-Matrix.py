class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        resSize = len(grid) - 2
        maxLocal = [[] for i in range(resSize)]
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i + 3 > len(grid) or j + 3 > len(grid):
                    continue
                    
                maxVal = -1
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        maxVal = max(maxVal, grid[k][l])
                
                if maxVal != -1:
                    maxLocal[i].append(maxVal)
        
        return maxLocal