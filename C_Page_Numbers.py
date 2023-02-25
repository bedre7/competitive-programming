from collections import defaultdict, Counter
def runCase():
    pages = list(set(map(int, input().split(','))))
    pages.sort()
    
    format = []
    left = 0
    right = 1
    offset = pages[left]
    while right < len(pages):
        if pages[right] - pages[left] > 1:
            if pages[left] - offset == 0:
                format.append(str(offset))
            else:
                format.append(str(offset) + '-' + str(pages[left]))
            offset = pages[right]
        left += 1
        right += 1
    
    if offset == pages[-1]:
        format.append(str(offset))
    else:
        format.append(str(offset) + '-' + str(pages[-1]))

    print(','.join(format))

if __name__ == '__main__':
    runCase()