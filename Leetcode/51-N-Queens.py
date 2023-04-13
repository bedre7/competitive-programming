class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        solution = []
        board = [['.'] * n for i in range(n)]
        output = []
        
        def backtrack(r):
            if r == n:
                output.append([''.join(row) for row in board])
                return 
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))
                board[r][c] = 'Q'
                
                backtrack(r + 1)
                
                col.remove(c)
                posDiag.remove((r + c))
                negDiag.remove((r - c))
                board[r][c] = '.'
        
        backtrack(0)
        return output