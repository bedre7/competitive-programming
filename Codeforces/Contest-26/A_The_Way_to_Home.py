from collections import defaultdict, Counter, deque

def runCase():
    n, d = map(int, input().split())
    spots = [bool(int(c)) for c in input()]
    queue = deque([[0, 0]])
    # print(spots)
    while queue:
        curr, jumps = queue.popleft()
        if curr == n - 1:
            return print(jumps)
        for i in range(curr + d, curr, -1):
            # print(curr, i)
            if i < n and spots[i]:
                queue.append([i, jumps + 1])
                break
    
    print(-1)


if __name__ == '__main__':
     # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()
