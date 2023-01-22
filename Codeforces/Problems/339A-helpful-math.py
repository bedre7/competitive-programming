def solution():
    numbers = input().split('+')
    numbers.sort()
    return '+'.join(numbers)

print(solution())