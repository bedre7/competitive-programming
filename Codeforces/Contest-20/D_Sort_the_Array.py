from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    isIncreasing = False
    
    for i in range(1, n):
        if array[i-1] > array[i]:
            break
    else:
        print('yes')
        print(1, 1)
        return
    
    for i in range(1, n):
        if array[i-1] < array[i]:
            break
    else:
        print('yes')
        print(1, n)
        return
    
    start = end = -1
    currMax = array[0]
    decreased = 0
    for i in range(1, n):
        if array[i] > array[i - 1]:
            end = i - 1
            if isIncreasing and decreased > 1:
                print('no')
                break
            else:
                isIncreasing = True
        else:
            start = i
            decreased += 1

        if array[i] < currMax and end != -1: 
            return print('no')
        currMax = max(currMax, array[i])
    else:
        print('yes')
        print(start, end) 
    
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()