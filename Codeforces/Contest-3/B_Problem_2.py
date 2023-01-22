if __name__ == '__main__':
    first_str = input().lower()
    second_str = input().lower()

    for i in range(len(first_str)):
        if first_str[i] < second_str[i]:
            print(-1)
            break
        elif first_str[i] > second_str[i]:
            print(1)
            break
    else:
        print(0)