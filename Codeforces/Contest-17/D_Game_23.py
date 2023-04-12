def compressWord(word, k):
    if not word: return word
    left = 0
    for right in range(1, len(word)):
        if word[right] != word[left]:
            left = right
        if right - left + 1 == k:
            return compressWord(word[:left] + word[right + 1:], k)

    return word

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        word = input()
        k = int(input())
        print(compressWord(word, k))