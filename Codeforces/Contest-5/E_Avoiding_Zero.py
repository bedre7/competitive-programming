from collections import deque

def runCase(nums, N, secondCall = False):
    total = 0
    for num in nums:
        total += num
        if total == 0:
            break
    else:
        print("YES")
        print(*nums)
        return
    
    nums.sort()
    queue = deque(nums)

    if secondCall:
        answer = [queue.pop()]
    else:
        answer = [queue.popleft()]

    total = answer[0]
    lastPoped = -1
    while queue:
        if lastPoped == -1:
            if total + queue[0] != 0:
                answer.append(queue.popleft())
                lastPoped = 0
            elif total + queue[-1] != 0:
                answer.append(queue.pop())
                lastPoped = -1
            elif not secondCall:
                runCase(nums, N, True)
            else:
                print("NO")
                return
        elif lastPoped == 0:
            if total + queue[-1] != 0:
                answer.append(queue.pop())
                lastPoped = -1
            elif total + queue[0] != 0:
                answer.append(queue.popleft())
                lastPoped = 0
            else:
                print("NO")
                return
                
        total += answer[-1]
    
    print("YES")
    print(*answer)


if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        N = int(input())
        nums = list(map(int, input().split()))
        runCase(nums, N)