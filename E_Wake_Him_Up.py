def solution():
    n, k = map(int, input().split())
    theorems = list(map(int, input().split()))
    states = list(map(int, input().split()))

    max_notes = 0
    curr_notes = 0
    for i in range(len(states)):
        if states[i] == 0:
            temp = 0
            j = i
            while j < k + i and j < len(states):
                temp += theorems[j]
                j += 1
            max_notes = max(max_notes, curr_notes + temp)
            print(curr_notes + temp)
        else:
            curr_notes += theorems[i]

    print(max_notes)

solution()