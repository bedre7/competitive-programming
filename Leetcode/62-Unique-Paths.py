class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for i in range(m - 1):
            for j in range(len(row) - 2, -1, -1):
                row[j] += row[j + 1]
                
        return row[0]