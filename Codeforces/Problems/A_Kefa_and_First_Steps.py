from collections import defaultdict, Counter
def runCase():
    n = int(input())
    array = list(map(int, input().split()))

    left = 0
    maxLen = 1
    right = 1
    while right < n:
        if array[right] < array[right - 1]:
            maxLen = max(maxLen, right - left)
            left = right
        right += 1

    maxLen = max(maxLen, right - left)
    print(maxLen)

if __name__ == '__main__':
    runCase()