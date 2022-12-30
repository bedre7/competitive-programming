if __name__ == '__main__':
    K = int(input())
    rooms = input().split()
    my_map = {}
    
    for r in rooms:
        if r not in my_map:
            my_map[r] = 1
        else:
            my_map[r] += 1
    
    print(''.join([r for r in my_map if my_map[r] == 1]))