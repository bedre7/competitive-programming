class Coord:
    def __init__(self, i, j):
        self.i = i
        self.j = j

def runCase():
    N = int(input())

    board = []
    for _ in range(N):
        row = list(map(int, input()))
        board.append(row)

    def rotate(coord):
        return Coord(coord.j, N - coord.i - 1)

    flips = 0
    visited = set()
    for i in range(N):
        for j in range(N):
            at_0 = Coord(i, j)
            if (at_0.i, at_0.j) in visited: 
                continue

            at_90 = rotate(at_0)
            at_180 = rotate(at_90)
            at_270 = rotate(at_180)

            rotations = [at_0, at_90, at_180, at_270]

            ones = zeros = 0
            for coord in rotations:
                ones += board[coord.i][coord.j] == 1
                zeros += board[coord.i][coord.j] == 0
            
            flips += min(ones, zeros)

            for coord in rotations:
                visited.add((coord.i, coord.j))

    print(flips)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()