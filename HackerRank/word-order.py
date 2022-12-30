# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = int(input())
    my_map = {}
    
    for i in range(N):
        word = input()
        if word not in my_map:
            my_map[word] = 1
        else:
            my_map[word] += 1
        
    print(len(my_map))
    print(' '.join([str(val) for key, val in my_map.items()]))