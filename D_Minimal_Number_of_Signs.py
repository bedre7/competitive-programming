def solution():
    n = int(input())

    sample = ''
    allwords = []

    for i in range(n):
        allwords.append(input())

    sample = [''] * len(allwords[0])
    
    index = 0
    for i in range(len(allwords[0])):
        curr_char = allwords[0][i]
        if curr_char == '?':
            sample[index] = '?'
            index += 1
            continue

        isMatched = True
        isOptional = False
        for j in range(n):
            if allwords[j][i] == '?':
                isOptional = True
                break
            if curr_char != allwords[j][i]:
                break
        if isOptional:
            sample += '?'
        else:
            if isMatched:
                sample += curr_char
            else:
                sample += '?'

        index += 1
    print(''.join(sample))

solution()