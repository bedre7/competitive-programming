def get_next_index(s, size, index, color):   
    while index < size:
        if s[index] != color:
            index += 1
        else:
            return index
    return None

def solution():
    test_cases = int(input()) 

    for _ in range(test_cases):
        first_line = input().split()
        size, current_color = int(first_line[0]), first_line[1]
        s = input()

        if current_color == 'g':
            print(0)
            continue

        seconds = 0
        index = get_next_index(s, size, 0, current_color)

        curr_seconds = 0
        flag = False
        while index != None and index < size:
            if s[index] != 'g':
                if index == size - 1:
                    flag = True
                index = (index + 1) % size
                curr_seconds += 1
            else:
                seconds = max(seconds, curr_seconds)
                curr_seconds = 0
                next_index = get_next_index(s, size, index, current_color)

                if flag or not next_index:
                    break
                else:
                    index = next_index
                
        print(seconds)

solution()



