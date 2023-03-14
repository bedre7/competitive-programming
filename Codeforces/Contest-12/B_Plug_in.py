from collections import defaultdict, Counter
def runCase():
    string = input()
    stack = []

    for c in string:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    
    print(''.join(stack))

if __name__ == '__main__':
    runCase()