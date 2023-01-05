# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    A = defaultdict(list)
    
    for i in range(n):
        A[input()].append(str(i + 1))
    
    for _ in range(m):
        item = input()
        if item in A:
            print(' '.join(A[item]))
        else:
            print(-1)