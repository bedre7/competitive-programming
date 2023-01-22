def runCase():
    N, M = map(int, input().split())
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    def findSumAt(i, j):
        sum = board[i][j]

        dirs = [[1, 1], [-1, -1], [-1, 1], [1, -1]]

        for dir in dirs:
            row, col = i + dir[0], j + dir[1]
            while 0 <= row < N and 0 <= col < M:
                sum += board[row][col]
                row += dir[0]
                col += dir[1]
        
        return sum

    max_sum = 0
    for i in range(N):
        for j in range(M):
            max_sum = max(max_sum, findSumAt(i, j))
    
    print(max_sum)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()