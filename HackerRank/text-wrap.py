import textwrap

def wrap(string, max_width):
    output = ''
    
    for i in range(len(string)):
        output += string[i]
        if (i+1) % max_width == 0:
            output += '\n'
        
    return output
