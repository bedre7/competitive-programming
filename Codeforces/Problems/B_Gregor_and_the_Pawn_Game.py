from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    enemies = [int(cell) for cell in input()]
    pawns = [int(cell) for cell in input()]
    
    count = 0
    for i in range(n):
        if pawns[i] == 1:
            if i > 0 and enemies[i - 1] == 1:
                enemies[i - 1] = -1
            elif i < n - 1 and enemies[i + 1] == 1:
                enemies[i + 1] = -1
            elif enemies[i] == 0:
                enemies[i] = -1
            else:
                continue
            count += 1
    
    print(count)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()