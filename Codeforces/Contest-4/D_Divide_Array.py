def runCase():
    N = int(input())
    
    numbers = list(map(int, input().split()))
    
    positives, negatives = [], []
    for num in numbers:
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)

    zeros = [0]
    firstSet = [negatives[0]]
    negatives = negatives[1:]
    secondSet = positives

    if len(negatives) % 2 == 0:
        secondSet.extend(negatives)
    else:
        secondSet.extend(negatives[:len(negatives) - 1])
        zeros.append(negatives.pop())
    
    print(str(len(firstSet)) + " " + ' '.join(map(str, firstSet)))
    print(str(len(secondSet)) + " " + ' '.join(map(str, secondSet)))
    print(str(len(zeros)) + " " + ' '.join(map(str, zeros)))

if __name__ == '__main__':
    runCase()