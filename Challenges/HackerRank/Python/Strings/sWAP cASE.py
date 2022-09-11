def swap_case(s):
    new_sting = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                new_sting += i.lower()
            elif i.islower():
                new_sting +=i.upper()
        else:
            new_sting += i   
    
    return new_sting

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)