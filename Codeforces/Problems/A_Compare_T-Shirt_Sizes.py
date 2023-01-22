if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        left, right = map(str, input().split())
        if left[-1] == right[-1]:
            if left[-1] == 'S':
                if len(left) > len(right):
                    print('<')
                elif len(left) < len(right):
                    print('>')
                else:
                    print('=')
            else:
                if len(left) > len(right):
                    print('>')
                elif len(left) < len(right):
                    print('<')
                else:
                    print('=')
        else:
            if left[-1] > right[-1]:
                print('<')
            else:
                print('>')