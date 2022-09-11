def count_substring(string, sub_string):
    string_len = len(string)
    sub_string_len = len(sub_string)
    counter = 0
    for i in range(0,string_len - sub_string_len + 1):
        if string[i:i+sub_string_len] == sub_string:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)