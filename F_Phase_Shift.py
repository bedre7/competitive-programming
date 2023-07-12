from collections import defaultdict, Counter, deque
import string

def runCase():
    n = int(input())
    s = input()
    letters = deque([c for c in string.ascii_lowercase])
    mapping = defaultdict(str)
    mapped = []
    used = set()
    for c in s:
        if c not in mapping:
            for letter in letters:
                if (letter, c) in used or letter == c: continue
                mapping[c] = letter
                used.add((c, letter))
                letters.remove(letter)
                break
        mapped.append(mapping[c])

    print(''.join(mapped))
                
if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()