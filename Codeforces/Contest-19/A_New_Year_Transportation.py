from collections import defaultdict, Counter, deque

def runCase():
    n, t = map(int, input().split())
    portals = list(map(int, input().split()))
    world = defaultdict(int)
    
    for i in range(n - 1):
        world[i + 1] = portals[i] + i + 1

    start = 1
    while world[start] != 0:
        if world[start] == t:
            print('YES')
            return
        start = world[start]

    print('NO')   
    
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()