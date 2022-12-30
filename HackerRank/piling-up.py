# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N = int(input())
        cubes = list(map(int, input().split()))
        upper = 1 << 31
        
        while cubes:
            wider = cubes[-1]
            if cubes[0] > cubes[-1]:
                wider = cubes[0]
                cubes.pop(0)
            else:
                cubes.pop()
            
            if wider > upper:
                print("No")
                break
            upper = wider
                
        else:
            print("Yes")
