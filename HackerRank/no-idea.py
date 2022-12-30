# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = map(int, input().split())
    array = input().split()
    A = set(input().split())
    B = set(input().split())
    happiness = 0
    
    for i in range(n):
        if array[i] in A:
            happiness += 1
        if array[i] in B:
            happiness -= 1
        
    print(happiness)