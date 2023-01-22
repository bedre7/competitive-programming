def runCase():
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    winners = 0
    for score in scores:
        if score >= scores[K - 1] and score > 0:
            winners += 1

    print(winners)

if __name__ == '__main__':
    runCase()