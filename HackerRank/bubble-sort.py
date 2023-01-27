def countSwaps(a):
    swaps, n = 0, len(a)
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                swapped = True
                swaps += 1
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swapped:
            break;
        
    print(f'Array is sorted in {swaps} swaps.')
    print("First Element:", a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)