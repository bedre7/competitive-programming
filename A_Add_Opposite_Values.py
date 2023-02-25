from collections import defaultdict, Counter
def runCase():
    n = int(input())
    string = input()
    left = 0
    right = n - 1

    while left <= right:
        if string[left] != string[right]:
            left += 1
            right -= 1
        else:
            break 
    
    print(right - left + 1)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()