from collections import defaultdict, Counter, deque

def runCase():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))

    ones = [0] * 31
    mask = 1
    for i in range(31):
        for a in array:
            if a & mask:
                ones[i] += 1
        mask <<= 1

    for i in range(30, -1, -1):
        if ones[i] != n and k >= n - ones[i]:
            k -= n - ones[i]
            ones[i] = n
    
    ans = 0
    mask = 1
    for i in range(31):
        if ones[i] == n:
            ans |= mask
        mask <<= 1

    print(ans)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()