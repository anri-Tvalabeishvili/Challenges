# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
set_A = set(input().split())
number_of_command = int(input())

for i in range(number_of_command):
    command = (input().split())
    new_set = set((input().split()))
    
    if command[0] == "intersection_update":
        set_A.intersection_update(new_set)
    elif command[0] == "update":
        set_A.update(new_set)
    elif command[0] == "symmetric_difference_update":
        set_A.symmetric_difference_update(new_set)
    elif command[0] == "difference_update":
        set_A.difference_update(new_set)
        

sum_new_set_A = sum(set(map(int,set_A)))
print(sum_new_set_A)