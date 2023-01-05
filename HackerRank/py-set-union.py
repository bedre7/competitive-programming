# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    A = set(input().split())
    m = int(input())
    B = set(input().split())
    
    print(len(A.union(B)))