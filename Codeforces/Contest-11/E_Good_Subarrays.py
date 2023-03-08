from collections import defaultdict, Counter
def runCase():
    n = int(input())
    array = [int(c) for c in input()]
    prefix = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix[i] += prefix[i - 1] + array[i - 1]
    count = 0
    for i in range(n):
        for j in range(i, n):
            if prefix[j + 1] - prefix[i] == j - i + 1:
                count += 1
    # curr = 0
    # left = 0

    # for right in range(n):
    #     curr += array[right]
    #     if curr == right - left + 1:
    #         count += 1
    #     elif curr > right - left + 1:
    #         curr -= array[left]
    #         left += 1
    print(count)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()