from collections import defaultdict, Counter

def makeGood(string, char):
    if len(string) == 1:
        return 1 if string != char else 0
    
    firsthalf = string[:len(string) // 2]
    secondhalf = string[len(string) // 2:]
    leftCost = len(firsthalf) - Counter(firsthalf)[char] + makeGood(secondhalf, chr(ord(char) + 1))
    rightCost = len(secondhalf) - Counter(secondhalf)[char] + makeGood(firsthalf, chr(ord(char) + 1))
    
    return min(leftCost, rightCost)

def runCase():
    n = int(input())
    string = input()
    print(makeGood(string, 'a'))

def main():
    tests = int(input())

    for _ in range(tests):
        runCase()

main()