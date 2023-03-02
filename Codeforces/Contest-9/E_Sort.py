from collections import defaultdict, Counter
def runCase():
    n = int(input())
    a = list(map(int, input().split()))
    left = 0
    for right in range(1,n):
        if a[left] > a[right]:
            a[left], a[right] = a[right], a[left]
        left += 1
        
    left = 0
    for right in range(1, n):
        if a[left] > a[right]:
            return 'NO'
        left += 1
    
    return 'YES'

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        print(runCase())