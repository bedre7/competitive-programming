from collections import defaultdict, Counter
def runCase():
    brackets = input()
    stack = []

    for c in brackets:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
    
    print(len(brackets) - len(stack))

if __name__ == '__main__':
    runCase()