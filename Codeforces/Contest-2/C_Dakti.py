if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        words = input().split()

        sorted = [''] * len(words)
        for word in words:
            order = []
            filtered = []
            for char in word:
                if char.isdigit():
                    order.append(char)
                    # order += char
                else:
                    # filtered += char
                    filtered.append(char)

            sorted[int(''.join(order)) - 1] = ''.join(filtered)
            
        # O(N^2)
            
        print(' '.join(sorted))