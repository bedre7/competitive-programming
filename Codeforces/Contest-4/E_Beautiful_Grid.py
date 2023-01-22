from math import ceil

def runCase():
    N = int(input())
    grid = []

    for _ in range(N):
        grid.append(input())
    
    edge = 0
    for i in range(ceil(N/2)):
        degree0 = grid[0][edge:N - edge]
        degree90 = []
        for j in range(N - edge - 1, -1, edge - 1):
            degree90.append(grid[edge][j])
        
        # degree180 = []
        # for j in range(N - edge - 1, -1, edge - 1):
        #     degree90.append(grid[N - edge - 1][j])


if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()