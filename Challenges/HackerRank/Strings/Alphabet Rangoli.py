def print_rangoli(size):
    # your code goes here
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    required_letters = alphabet[0:size][::-1]
    
    # top half
    for i in range(1,size+1):
        line_length = 4*size -3
        first_half = required_letters[:i]
        second_half = required_letters[:i-1][::-1]
        whole_line = first_half + second_half
        
        first_half = '-'.join([str(elem) for elem in whole_line])
        
        finished_line = first_half.center(line_length,"-")
        
        print(finished_line)
        
    # lower half
    for i in range(size-1,0,-1):
        line_length = 4*size -3
        first_half = required_letters[:i]
        second_half = required_letters[:i-1][::-1]
        whole_line = first_half + second_half
        
        first_half = '-'.join([str(elem) for elem in whole_line])
        finished_line = first_half.center(line_length,"-")
        print(finished_line)
        
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)