from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    s1, s2 = input(), input()
    parents = defaultdict(str)
    for i in range(ord('a'), ord('z') + 1):
        parents[chr(i)] = chr(i)

    def find(char):
        p = parents[char]
        while p != parents[p]:
            parents[p] = parents[parents[p]]
            p = parents[p]
        return p
    def union(c1, c2):
        p1, p2 = find(c1), find(c2)
        if p1 == p2: return False
        parents[p1] = p2
        return True
    
    swaps = []
    for i in range(n):
        if union(s1[i], s2[i]):
            swaps.append((s1[i], s2[i]))
    
    print(len(swaps))
    for swap in swaps:
        print(*swap)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()