class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        [Xs, Os] = self.countPlayers(board)
        
        if Xs != Os and Xs != Os + 1:
            return False
        
        if self.hasWon(board, 'O'):
            if self.hasWon(board, 'X'):
                return False
            
            return Xs == Os
            
        if self.hasWon(board, 'X'):
            return Xs == Os + 1
                
        return True
        
    def countPlayers(self, board: List[str]) -> []:
        Xs = Os = 0
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    Xs += 1
                elif board[i][j] == 'O':
                    Os += 1

        return [Xs, Os]
    
    def hasWon(self, board: List[str], player) -> bool:
        # check row win
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            
        # check col win
        for i in range(len(board)):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
        
        # check diagonal win
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        
        return False