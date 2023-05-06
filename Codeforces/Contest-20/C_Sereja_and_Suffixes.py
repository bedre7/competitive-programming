from collections import defaultdict, Counter, deque

def runCase():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    distincts = len(set(array))
    lastSeen = defaultdict(int)
    for i in range(n):
        lastSeen[array[i]] = i
    distinctOnes = [distincts] * n
    
    x = 0
    for i in range(n - 1):
        if lastSeen[array[i]] == i:
            x += 1
        distinctOnes[i + 1] -= x
    distinctOnes[-1] = 1

    for _ in range(m):
        l = int(input())
        print(distinctOnes[l - 1])

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()