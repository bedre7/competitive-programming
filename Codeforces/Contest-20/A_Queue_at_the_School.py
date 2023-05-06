from collections import defaultdict, Counter, deque

def runCase():
    n, t = map(int, input().split())
    children = list(input())

    for _ in range(t):
        i = 1
        while i < n:
            if children[i] == 'G' and children[i-1] == 'B':
                children[i] = 'B'
                children[i-1] = 'G'
                i += 1
            i += 1
    
    print(''.join(children))


if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()