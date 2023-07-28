from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    s = input()
    stack = []
    res = 0
    for c in s:
        if not stack: stack.append(c)
        elif c != stack[-1]: stack.pop()
        else: stack.append(c)
        res = max(res, len(stack))
    print(res + 1)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()