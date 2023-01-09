if __name__ == '__main__':
    size = int(input())

    upper = list(map(str, input()))
    if size == 1:
        print(''.join(upper).replace('?', 'c'))
    else:
        for i in range(1, size):
            lower = list(map(str, input()))

            for j in range(len(lower)):
                if upper[j] == lower[j] == '?':
                    continue
                if upper[j] != lower[j]:
                    if upper[j] == '?' or lower[j] == '?':
                        lower[j] = upper[j] if upper[j] != '?' else lower[j]
                    else:
                        lower[j] = '*'
            
            upper = lower
        
        print(''.join(upper).replace('?', 'c').replace('*', '?'))
            
