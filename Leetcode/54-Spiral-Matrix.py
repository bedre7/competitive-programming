class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        visited = {}
        index = 0
        output = []
        
        def isInBound(i, j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])
        size = len(matrix) * len(matrix[0])
        row = col = 0
        
        r, c = dirs[index]
        while len(output) != size:
            if isInBound(row, col) and (row, col) not in visited:
                output.append(matrix[row][col])
                visited[(row, col)] = True
            
                row += r
                col += c
            else:
                row -= r
                col -= c
                index = (index + 1) % 4
                r, c = dirs[index]
                row += r
                col += c
                
        return output