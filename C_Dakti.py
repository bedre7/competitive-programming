def solution():
    test_cases = int(input())

    for _ in range(test_cases):
        words = input().split()

        ordered = [''] * len(words)
        for word in words:
            order = ''
            filtered = ''
            for char in word:
                if char.isdigit():
                    order += char
                else:
                    filtered += char
            ordered[int(order) - 1] = filtered
        print(' '.join(ordered))

solution()