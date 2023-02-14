def runCase():
    n = int(input())
    string = input()
    if n == 0: return 0

    left = 0
    right = n - 1

    while left < right:
        if string[left] != string[right]:
            left += 1
            right -= 1
        else:
            break

    return right - left + 1

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        print(runCase())