def runCase():
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    if a1 + b2 == b1 == a2 or b1 + a2 == a1 == b2 or a1 + a2 == b1 == b2 or b1 + b2 == a1 == a2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()