import string
from collections import defaultdict, Counter
def runCase():
    word = input()
    if len(word) < 26:
        return -1

    alphabet = set(string.ascii_uppercase)

    left = right = 0
    occur = defaultdict(int)

    while right < len(word):
        if word[right] != '?':
            if occur[word[right]] == 0:
                occur[word[right]] += 1
            else:
                left = right
                occur.clear()
                occur[word[right]] += 1

        if right - left + 1 == 26:
            nice = [c for c in word[left:right + 1]]
            missing = alphabet.difference(nice)

            for i in range(26):
                if nice[i] == '?':
                    nice[i] = missing.pop()
            
            if not missing:
                output = word[:left] + ''.join(nice) + word[right + 1:]
                return output.replace('?','A')
            else:
                if word[left] != '?':
                    occur[word[left]] -= 1
                left += 1

        right += 1
    
    return -1

if __name__ == '__main__':
    print(runCase())