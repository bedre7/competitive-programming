def solution():
    A = input().split()
    n = int(input())
    
    for i in range(n):
        other = input().split()
        if len(other) >= len(A):
            return False
        
        for c in other:
            if c not in A:
                return False
    
    return True

print(solution())