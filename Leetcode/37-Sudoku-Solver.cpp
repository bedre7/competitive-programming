class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        backtrack(board, 0);
    }
    bool backtrack(vector<vector<char>>& board, int index) {
        if (index >= 81) return true;
        int i = index / 9;
        int j = index % 9;
        if (board[i][j] != '.') return backtrack(board, index + 1);
            
        for (char c = '1'; c <= '9'; c++){
            if (!isSafe(board, i, j, c)) continue;
            
            board[i][j] = c;
            if (backtrack(board, index + 1))
                return true;
            else    //backtrack
                board[i][j] = '.';
        }

        return false;
    }
    bool isSafe(vector<vector<char>>& board, int row, int col, char c){
        //check rows and cols
        for (int i = 0; i < 9; i++){
            if (board[i][col] == c || board[row][i] == c) return false;
        }
        //check diagonals
        int blockRow = row - row % 3;
        int blockCol = col - col % 3;
        for(int i = blockRow; i < blockRow + 3; i++)
            for(int j = blockCol; j < blockCol + 3; j++)
                if (board[i][j] == c) return false;

        return true;
    }
};