from collections import defaultdict, Counter
def runCase():
    word = input()
    if len(word) < 26:
        return -1

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    left = right = 0
    occur = defaultdict(int)

    while right < len(word):
        if word[right] != '?':
            if occur[word[right]] == 0:
                occur[word[right]] += 1
            else:
                left = right
                occur.clear()
                occur[word[right]] += 1 if word[right] != '?' else 0

        if right - left + 1 == 26:
            empty = 26 - sum(occur.values())
            nice = [''] * 26
            filled = 0
            j = 0
            ok = True
            for i in range(26):
                if not ok: break
                if word[left + i] != '?':
                    nice[i] = word[left + i]
                else:
                    while j < 26:
                        if occur[alphabet[j]] == 0:
                            if filled >= empty:
                                while left < len(word) and word[left] != '?':
                                    occur[word[left]] -= 1
                                    left += 1
                                ok = False
                            nice[i] = alphabet[j]
                            filled += 1
                            j += 1
                            break
                        j += 1
            else:
                return ''.join(nice)

        right += 1
    
    return -1

if __name__ == '__main__':
    print(runCase())