from collections import defaultdict, Counter
def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    so_far = 0
    ans = 0
    
    for i in range(n):
        if so_far <= array[i]:
            ans += 1
            so_far += array[i]

    print(ans)

if __name__ == '__main__':
    runCase()