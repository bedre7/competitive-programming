def solve():
    n = int(input())

    array = list(map(int, input().split()))

    odds = evens = 0
    for num in array:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    if evens and odds:
        array.sort()

    print(*array)
        
if __name__ == '__main__':
    solve()