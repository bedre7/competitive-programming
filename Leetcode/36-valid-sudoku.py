class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colsAreValid = self.validateRowAndCols(board)
        if not colsAreValid: return False
        
        return self.validateGrids(board)
            
    def validateRow(self, row: List[str]) -> bool:
        numsmap = {}
        for cell in row:
            if cell.isdigit():
                if cell in numsmap:
                    return False
                numsmap[cell] = 1
        return True
    
    def validateRowAndCols(self, board: List[List[str]]) -> bool:
        numsmap = {}
        for i in range(len(board)):
            numsmap = {} 
            rowIsValid = self.validateRow(board[i])
            if not rowIsValid: return False
            for j in range(len(board)):
                if board[j][i].isdigit():
                    if board[j][i] in numsmap:
                        return False
                    numsmap[board[j][i]] = 1
        
        return True
    
    def validateGrids(self, board: List[List[str]]) -> bool:
        numsmap = {}
        
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                numsmap = {}
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l].isdigit():
                            if board[k][l]in numsmap:
                                return False
                            numsmap[board[k][l]] = 1
                
        return True
