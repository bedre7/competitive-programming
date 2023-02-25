from collections import defaultdict, Counter
def runCase():
    year = int(input())

    i = year + 1
    while True:
        if len(Counter(str(i)).keys()) == 4:
            return i
        i += 1

if __name__ == '__main__':
    print(runCase())