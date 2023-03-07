def runCase():
    # n = int(input())
    # array = list(map(int, input().split()))
    print('YES' if input().upper() == 'YES' else 'NO')

if __name__ == '__main__':
    testCase = int(input())
    # testCase = 1

    for _ in range(testCase):
        runCase()