if __name__ == '__main__':
    hello = 'hello'
    said = input()

    i = 0
    for char in said:
        if char == hello[i]:
            i += 1
        if i == 5:
            break
    
    if i == 5:
        print('YES')
    else:
        print('NO')