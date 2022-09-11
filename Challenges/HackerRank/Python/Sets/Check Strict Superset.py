# Enter your code here. Read input from STDIN. Print output to STDOUT
superset = set(input().split())

number_of_sets = int(input())

Confirmation = True

for i in range(number_of_sets):
    new_set = set(input().split())
    if len(superset) < len(new_set) or len(new_set.difference(superset)) != 0: 
        Confirmation = False
        break
    
print(Confirmation)


