def runCase():
    input()
    
    board = []
    N = 8
    for _ in range(N):
        board.append(input())

    for i in range(1, N - 1):
        for j in range(1, len(board[i]) - 1):
            if board[i][j] == '.':
                continue
            if board[i][j] == board[i - 1][j - 1] == board[i - 1][j + 1] == board[i + 1][j - 1] == board[i + 1][j + 1]:
                print(i + 1, j + 1)
                return


if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()