# from collections import defaultdict

def solution():
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        arr = input().split()
        string = input()

        for i in range(n):
            curr_char = string[i]
            curr_num = arr[i]
            if curr_num == -1:
                continue
            shouldEnd = False
            for j in range(i + 1, n):
                if curr_num == arr[j] and curr_char != string[j]:
                    arr[j] = -1 #To avoid checking again
                    print("NO")
                    shouldEnd = True
                    break
            if shouldEnd:
                break
        else:
            print("YES")
                

solution()