def superDigit(n, k):
    if len(n) == 1:
        return n
    digits = n

    ans = 0
    while len(digits) > 1:
        ans = 0
        for digit in digits:
            ans += int(digit)
        digits = str(ans)

    return superDigit(str(ans * k), 1) if k > 1 else ans

print(superDigit("9875", 4))