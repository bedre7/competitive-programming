def solution():
    first_str = input().lower()
    second_str = input().lower()

    for i in range(len(first_str)):
        if first_str[i] < second_str[i]:
           return -1
        elif first_str[i] > second_str[i]:
            return 1
    
    return 0

print(solution())