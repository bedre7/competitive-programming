from collections import defaultdict, Counter
def runCase():
    n = int(input())
    boys = list(map(int, input().split()))
    m = int(input())
    girls = list(map(int, input().split()))

    boys.sort()
    girls.sort()

    left = 0
    pairs = 0
    while left < len(boys):
        for right in range(len(girls)):
            if girls[right] != -1 and abs(boys[left] - girls[right]) <= 1:
                pairs += 1
                girls[right] = -1
                break
        left += 1

    print(pairs)

if __name__ == '__main__':
    runCase()