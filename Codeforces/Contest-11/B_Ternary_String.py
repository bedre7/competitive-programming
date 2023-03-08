from collections import defaultdict, Counter
def runCase():
    string = input()
    window = defaultdict(int)
    minLen = len(string)
    found = False

    left = 0
    for right in range(len(string)):
       window[string[right]] += 1
       while len(window.keys()) == 3:
           minLen = min(minLen, right - left + 1)
           window[string[left]] -= 1
           found = True
           if window[string[left]] == 0:
               del window[string[left]]
           left += 1
    
    print(minLen if found else 0)
           

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()