def split_and_join(line):
    # write your code here
    splited_line = line.split(" ")
    joined_line = "-".join(splited_line)
    return joined_line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)