from collections import deque
def runCase():
    s = deque(input())
    t = []
    u = []

    for c in s:
       if t and c > t[-1]:
           u.append()

    print(''.join(t + u))    

if __name__ == '__main__':
    runCase()