class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_col, zeros_col = [0] * n, [0] * n
        ones_row, zeros_row = [0] * m, [0] * m
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones_row[i] += 1
                    ones_col[j] += 1
                else:
                    zeros_row[i] += 1
                    zeros_col[j] += 1
        
        diff = []
        for i in range(m):
            diff.append([])
            for j in range(n):
                diff[i].append(ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j])
                
        return diff
        