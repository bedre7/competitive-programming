def solve():
    N = int(input())
    
    numbers = list(map(int, input().split()))

    negatives = []
    positives = []
    zeros = []

    for num in numbers:
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
        else:
            zeros.append(num)

    firstSet = [negatives.pop()]
    secondSet = positives

    if len(negatives) % 2 != 0:
        zeros.append(negatives.pop())
    
    secondSet.extend(negatives)
    
    print(len(firstSet), *firstSet)
    print(len(secondSet), *secondSet)
    print(len(zeros), *zeros)

if __name__ == '__main__':
    solve()