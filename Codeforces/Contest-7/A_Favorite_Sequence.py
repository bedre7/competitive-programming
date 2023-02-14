from collections import deque
def runCase():
    n = int(input())
    num = list(map(int, input().split()))

    original = []
    queue = deque(num)
    for i in range(n):
        if i % 2 == 0:
            original.append(queue.popleft())
        else:
            original.append(queue.pop())
    
    print(*original)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()