def solution():
    size = int(input())
    members = input().split()
    bad_ones = input().split()

    count = 0
    for name in members:
        if len(name) % len(set(name)) == 0 and name not in bad_ones:
            count += 1

    print(count)

solution()