if __name__ == '__main__':
    N = int(input())
    py_list = []
    for i in range(N):
        line = input().split()
        if line[0] == 'insert':
            py_list.insert(int(line[1]), int(line[2]))
        elif line[0] == 'remove':
            py_list.remove(int(line[1]))
        elif line[0] == 'append':
            py_list.append(int(line[1]))
        elif line[0] == 'sort':
            py_list.sort()
        elif line[0] == 'pop':
            py_list.pop()
        elif line[0] == 'reverse':
            py_list.reverse()
        elif line[0] == 'print':
            print(py_list)