class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                curr_sum = (grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                                            + grid[i][j] + 
                            grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1])
                
                max_sum = max(max_sum, curr_sum)
                
        return max_sum