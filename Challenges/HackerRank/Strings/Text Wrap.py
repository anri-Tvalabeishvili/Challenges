import textwrap

def wrap(string, max_width):
    string_len = len(string)
    remainder = string_len % max_width
    count = 0
    while True:
        if count >= string_len:
            break
        print(string[count:count+max_width])
        count = count + max_width
        
        
    return string[-1:-remainder]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)