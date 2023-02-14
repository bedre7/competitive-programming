def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    left = 0
    right = 1

    while right < n:
        if array[left] < array[right]:
            break
        right += 1
        left += 1
    else:
        return 'YES'

    while right < n:
        if array[left] > array[right]:
            break
        right += 1
        left += 1
    else:
        return 'YES'
    left = 0
    right = n - 1

    while left < right:
        if left + 1 < right:
            if array[left] < array[left + 1]:
                break
        if right - 1 > left:
            if array[right] < array[right - 1]:
                break
        left += 1
        right -= 1
    else:
        return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        print(runCase())