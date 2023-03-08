from collections import defaultdict, Counter
def runCase():
    N = int(input())
    array = list(map(int, input().split()))
    copy = array.copy()
    array.sort()

    ans = []
    for n in copy:
        if n == array[-1]:
            ans.append(n - array[-2])
        else:
            ans.append(n - array[-1])
    
    print(*ans)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()