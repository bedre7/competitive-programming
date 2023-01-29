def runCase():
    N = int(input())

    numbers = list(map(int, input().split()))

    numbers.sort()
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) > 1:
            return "NO"
    
    return "YES"

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        print(runCase())