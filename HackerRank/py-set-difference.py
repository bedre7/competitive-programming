# Enter your code here. Read input from STDIN. Print output to STDOUT
english_len = input()
english = set(input().split())
french_len = input()
french = set(input().split())

print(len(english.difference(french)))