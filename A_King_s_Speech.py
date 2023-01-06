def solution():
    test_cases = int(input())

    for _ in range(test_cases):
        word = input()

        print(word[:2] + '... ' + word + '?')

solution()