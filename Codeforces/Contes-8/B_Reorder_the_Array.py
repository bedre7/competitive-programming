def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()

    left = 0
    right = n

    if sum(array[:right]) == sum(array[right:]):
        print(-1)
    else:
        print(*array)

if __name__ == '__main__':
    runCase()