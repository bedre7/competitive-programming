def runCase():
    # n = int(input())
    # array = list(map(int, input().split()))
    string = input()
    print(''.join(list(map(lambda s: s[0].upper() + s[1:], string.split(' ')))))

if __name__ == '__main__':
    # testCase = int(input())
    testCase = 1

    for _ in range(testCase):
        runCase()