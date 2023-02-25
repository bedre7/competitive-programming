from collections import defaultdict, Counter
def runCase():
    n, m = map(int, input().split())
    dorms = list(map(int, input().split()))
    rooms = list(map(int, input().split()))

    left = 0
    so_far = 0
    for room in rooms:
        while left < n and so_far + dorms[left] < room:
            so_far += dorms[left]
            left += 1
        
        roomNo = room - so_far
        print(left + 1, roomNo)

if __name__ == '__main__':
    runCase()