class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        N, M = len(board), len(board[0])
        def isSafe(row, col, char):
            for i in range(N):
                if (board[i][col] == char or board[row][i] == char):
                    return False
            blockRow, blockCol = row - row % 3, col - col % 3
            for i in range(blockRow, blockRow + 3):
                for j in range(blockCol, blockCol + 3):
                    if board[i][j] == char: return False
                    
            return True
        
        def backtrack(index):
            if index >= N * M: return True
            i = index // N
            j = index % N
            if board[i][j] != '.': return backtrack(index + 1)
            
            for char in "123456789":
                if isSafe(i, j, char):
                    board[i][j] = char
                    if backtrack(index + 1):
                        return True
                    else:
                        board[i][j] = '.'
                    
            return False
        
        backtrack(0)