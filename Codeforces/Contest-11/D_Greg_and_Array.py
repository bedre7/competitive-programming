from collections import defaultdict, Counter
def runCase():
    n, m, k = map(int, input().split())
    array = list(map(int, input().split()))
    ops = []
    for _ in range(m):
        ops.append(list(map(int, input().split())))
    
    prefix = [0] * (m + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        prefix[x - 1] += 1
        prefix[y] -= 1

    for i in range(1, m + 1):
        prefix[i] += prefix[i - 1]
    
    prefix = prefix[:-1]
    pre = [0] * (n + 1)
    for i in range(m):
        op = prefix[i]
        pre[ops[i][0] - 1] += op * ops[i][2]
        pre[ops[i][1]] -= op * ops[i][2]
    
    for i in range(1, n + 1):
        pre[i] += pre[i - 1]
    
    for i in range(n):
        array[i] += pre[i]
    print(*array)

if __name__ == '__main__':
    runCase()