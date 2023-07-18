from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    string = input()
    count = [0, 0]
    for c in string:
        count[int(c)] += 1

    print(abs(count[0] - count[1]))

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()