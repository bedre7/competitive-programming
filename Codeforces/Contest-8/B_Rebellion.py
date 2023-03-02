def runCase():
    n = int(input())
    array = list(map(int, input().split()))

    operations = 0
    left = right = 0

    while right < n:
        while right < n and array[right] >= array[left]:
            right += 1
            if array[left] == 0: left += 1
        if right < n:
            array[-1] += right - left
            operations += right - left
            left = right
            right += 1
    
    print(operations)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()