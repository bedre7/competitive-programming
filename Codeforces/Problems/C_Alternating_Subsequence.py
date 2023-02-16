def runCase():
    n = int(input())
    array = list(map(int, input().split()))

    array.sort()
    positives, negatives = [], []
    for num in array:
        if num > 0: positives.append(num)
        else: negatives.append(num)
    
    subseq = []
    while positives and negatives:
        subseq.append(positives.pop())
        subseq.append(negatives.pop())
    
    if subseq and subseq[-1] < 0 and positives:
        subseq.append(positives.pop())
    # elif subseq and subseq[-1] > 0 and negatives:
    #     subseq.append(negatives.pop())
    
    print(subseq)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()