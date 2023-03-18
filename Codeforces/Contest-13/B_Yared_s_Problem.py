from collections import defaultdict, Counter

def solve(array, n):
    return "YES"

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    left = 0
    for right in range(1, n):
        if array[right] - array[left] > 1:
            print("NO")
            return
        left += 1
    
    print("YES")

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        runCase()