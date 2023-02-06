from collections import deque
def runCase():
    n = int(input())

    nums = list(map(int, input().split()))
    nums.sort()

    queue = deque(nums)

    zsorted = []
    for i in range(n):
        if i % 2 == 0:
            zsorted.append(queue.popleft())
        else:
            zsorted.append(queue.pop())

    print(*zsorted)

if __name__ == '__main__':
    runCase()