# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_try = int(input())

for i in range(number_of_try):
    len_of_set_A = int(input())
    set_A = set(input().split())
    len_of_set_B = int(input())
    set_B = set(input().split())
    
    if len(set_A) < len(set_B) and len(set_A.difference(set_B)) == 0:
        print("True")
    else:
        print("False")