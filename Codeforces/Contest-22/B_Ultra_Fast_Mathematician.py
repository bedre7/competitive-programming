from collections import defaultdict, Counter, deque

def runCase():
    first = input()
    second = input()
    answer = []

    for i in range(len(first)):
        ans = str(int(first[i]) ^ int(second[i]))
        answer.append(ans)
    
    print(''.join(answer))

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()