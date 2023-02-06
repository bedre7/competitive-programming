def solve():
    n = int(input())

    array = list(map(int, input().split()))

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if array[j] + array[j + 1] % 2 != 0:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
        
        if not swapped:
            break
    
    print(*array)

if __name__ == '__main__':
    solve()