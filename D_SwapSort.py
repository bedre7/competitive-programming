from collections import defaultdict, Counter, deque
def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    queue2 = deque(array)
    fixed = []
    for i in range(n):
        fixed.append([array[i], i])

    fixed.sort(key=lambda x: x[1])
    queue = deque(fixed)
    print(queue)
    swaps = []
    while queue:
        if queue[-1][0] > queue[0][0] and queue[-1][1] < queue[0][1]:
            swaps.append([queue[0][1], queue[-1][1]])
        queue.pop()
        if queue: queue.popleft()
        queue2.pop()
        if queue2: queue2.popleft()

    print(swaps)

if __name__ == '__main__':
    runCase()