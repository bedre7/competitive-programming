from collections import defaultdict, Counter, deque

def runCase():
    grid = [input() for _ in range(3)]
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != '.': return print(grid[i][0])
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != '.': return print(grid[0][i])
    
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '.': return print(grid[0][0])
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '.': return print(grid[0][2])
    return print ("DRAW")

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()