from collections import deque
def runCase():
    n = int(input())
    cards = list(map(int, input().split()))
    
    queue = deque(cards)
    s = d = 0
    
    dturn = False
    while queue:
        if not dturn:
            if queue[-1] > queue[0]:
                s += queue.pop()
            else:
                s += queue.popleft()
            dturn = True
        else:
            if queue[-1] > queue[0]:
                d += queue.pop()
            else:
                d += queue.popleft()
            dturn = False
    
    print(s, d)
        


if __name__ == '__main__':
    runCase()