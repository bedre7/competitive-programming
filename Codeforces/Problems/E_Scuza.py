from collections import defaultdict, Counter, deque

def runCase():
    N, Q = map(int, input().split())
    array = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    ans = {}
    steps = j = 0
    for q in sorted(queries):
        while j < N and array[j] <= q:
            steps += array[j]
            j += 1
        ans[q] = steps
    
    print(*[ans[q] for q in queries])
    
if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()