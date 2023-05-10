from collections import defaultdict, Counter, deque

def runCase():
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    queries = [0] * (n + 1)
    for _ in range(q):
        start, end = map(int, input().split())
        queries[start - 1] += 1
        queries[end] += -1
    
    for i in range(1, n):
        queries[i] += queries[i - 1]
    queries.pop()
    queries.sort(reverse=True)
    array.sort(reverse=True)

    maxSum = 0
    for i in range(n):
        maxSum += array[i] * queries[i]
    
    print(maxSum)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()