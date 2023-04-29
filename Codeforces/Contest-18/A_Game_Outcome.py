from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    board = []
    for _ in range(n):
        board.append(input().split())
    
    winning = 0
    rowSums = [0] * n
    colSums = [0] * n
    for i in range(n):
        rowSums[i] = sum([int(x) for x in board[i]])
        for j in range(n):
            colSums[j] += int(board[i][j])
    
    for i in range(n):
        for j in range(n):
            if colSums[j] > rowSums[i]:
                winning += 1
    
    print(winning)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()