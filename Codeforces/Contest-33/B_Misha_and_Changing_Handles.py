from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    used = set()
    parents = defaultdict(str)

    def find(name):
        p = parents[name]
        while p and p in parents:
            p = parents[p]
        return p
    initials = set()
    for _ in range(n):
        old, new = map(str, input().split())
        if old not in used:
            initials.add(old)
        used.add(new)
        parents[old] = new
    
    print(len(initials))
    for name in list(initials):
        print(name, find(name))

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()