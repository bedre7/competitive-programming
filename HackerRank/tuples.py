# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
numbers = tuple(map(int, input().split()))
print(hash(numbers))
