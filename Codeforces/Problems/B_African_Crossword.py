def solve():
    N, M = map(int, input().split())

    board = []
    for i in range(N):
        board.append([c for c in input()])
    
    def crossOut(row, col):
        wasCrossedOut = False
        for i in range(M):
            if i != col and board[row][i] == board[row][col].lower():
                board[row][i] = board[row][i].upper()
                wasCrossedOut = True

        for i in range(N):
            if i != row and board[i][col] == board[row][col].lower():
                board[i][col] = board[i][col].upper()
                wasCrossedOut = True

        if wasCrossedOut:
            board[row][col] = board[row][col].upper()

    for i in range(N):
        for j in range(M):
            if board[i][j] != '*':
                crossOut(i, j)

    encrypted = []
    for i in range(N):
        for j in range(M):
            if board[i][j].islower():
                encrypted.append(board[i][j])
    
    print(''.join(encrypted))

if __name__ == '__main__':
    solve()