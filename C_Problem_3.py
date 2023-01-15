if __name__ == '__main__':
    n = int(input())

    coins = list(map(int, input().split()))
    coins.sort()
    
    take = sum(coins)
    amount = len(coins)
    twin = 0

    for coin in coins:
        if take - coin > (twin + coin):
            take -= coin
            twin += coin
            amount -= 1
        else:
            break

    print(amount)