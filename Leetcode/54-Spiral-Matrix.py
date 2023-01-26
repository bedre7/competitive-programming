class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        up = left = 0
        right, down = len(matrix[0]) - 1, len(matrix) - 1

        spiral = []
        while left <= right and up <= down:
            for i in range(left, right + 1):
                spiral.append(matrix[up][i])
            up += 1
            if up > down:   break
            
            for i in range(up, down + 1):
                spiral.append(matrix[i][right])
            right -= 1
            if left > right:   break
            
            for i in range(right, left - 1, -1):
                spiral.append(matrix[down][i])
            down -= 1

            if up > down: break
            for i in range(down, up - 1, -1):
                spiral.append(matrix[i][left])
            left += 1
        
        return spiral