class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        
        while start <= end:
            mid = (end + start) // 2
            col = mid % len(matrix[0])
            row = mid // len(matrix[0])
            
            if matrix[row][col] < target:
                start = mid + 1
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                return True
        
        return False