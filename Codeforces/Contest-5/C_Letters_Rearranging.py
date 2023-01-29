def runCase():
    word = [c for c in input()]
    
    if word != word[::-1]:
        print(''.join(word))
        return

    for i in range(len(word) // 2):
        word[i], word[i+1] = word[i+1], word[i]
        if word != word[::-1]:
            print(''.join(word))
            break
    else:
        print(-1)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()