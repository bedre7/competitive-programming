from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    rotations = []
    for _ in range(n):
        rotations.append(int(input()))
    
    isPossible = False
    def rotate(currDegrees, at):
        nonlocal isPossible
        if isPossible: return currDegrees
        if at == n and currDegrees % 360 != 0: return currDegrees
        if currDegrees % 360 == 0 and at == n:  
            isPossible = True
            return 0

        clockwise = rotate(currDegrees + rotations[at], at + 1)
        counterClockwise = rotate(currDegrees - rotations[at], at + 1)
        
        return clockwise + counterClockwise
    
    rotate(0, 0)
    print('YES' if isPossible else 'NO')


if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()