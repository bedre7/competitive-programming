from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    sinks = set([i + 1 for i in range(n)])
    sources = set([i + 1 for i in range(n)])

    for i in range(n):
        line = list(map(int, input().split()))
        hasChild = False
        for j, v in enumerate(line):
            if v == 1:
                if j + 1 in sources:
                    sources.remove(j + 1)
                hasChild = True
        
        if hasChild and i + 1 in sinks:
            sinks.remove(i + 1)
    
    print(len(sources), *sources)
    print(len(sinks), *sinks)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()