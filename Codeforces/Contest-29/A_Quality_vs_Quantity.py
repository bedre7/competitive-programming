from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    array = sorted(list(map(int, input().split())), reverse=True)
    LS, RS = sum(array), 0
    print(array)
    for i in range(n):
        RS += array[i]
        LS -= array[i]
        print(RS, LS, i + 1, n - i - 1)
        if RS > LS and i + 1 < n - i - 1: return print("YES")
    print("NO")

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()