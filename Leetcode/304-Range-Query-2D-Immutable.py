class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        3 0 1 4 2
        5 6 3 2 1
        
        0 0 0 0 0 0
        0 3 3 4 8 10
        0 8 14  
        """
        self.m = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.prefix = [[0 for col in range(self.col + 1)] for row in range(self.row + 1)]
        
        for i in range(1, self.row + 1):
            for j in range(1, self.col + 1):
                self.prefix[i][j] = (self.prefix[i - 1][j] + 
                                     self.prefix[i][j - 1] + 
                                     self.m[i - 1][j - 1] - 
                                     self.prefix[i - 1][j - 1])
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2 + 1][col2 + 1] - 
                self.prefix[row1][col2 + 1] - 
                self.prefix[row2 + 1][col1] +
                self.prefix[row1][col1])
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)