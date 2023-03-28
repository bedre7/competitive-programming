import sys, threading
from collections import defaultdict, Counter

def runCase():
    l = int(input())
    x = 0
    commands = []
    for _ in range(l):
        commands.append(input().split())
    
    def solve():
        times = 0
        nonlocal x, commands
        
        while commands:
            if commands[-1][0] == 'end':
                last = commands.pop()
                while commands and commands[-1][0] != 'for':
                    if commands[-1][0] == 'add':
                        x += 1
                        if x > 2**32 - 1:
                            print('OVERFLOW!!!')
                            return
                    else:
                        x += solve()

                    last = commands.pop()
                # print(x)
                x *= int(commands[-1][1]) if commands else 1
                if len(last) > 1:
                    x *= int(last[1])
                
                if commands: commands.pop()
                if x > 2**32 - 1:
                    print('OVERFLOW!!!')
                    return
                
                return x
            
            elif commands[-1][0] == 'add':
                x += 1
                if x > 2**32 - 1:
                    print('OVERFLOW!!!')
                    return
                commands.pop()
        
        return x
        
    print(solve())
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()

"""10 15
for 10
    for 15
        add
        add
    end
    add
end

add
for 43
end
for 10
    for 15
      add
    end
    add
end

"""