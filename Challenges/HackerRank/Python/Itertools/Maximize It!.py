# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

first_line = input().split()
all_lists = []

for i in range(int(first_line[0])):
    new_list = [int(i) for i in input().split()][1:]
    all_lists.append(new_list)
    
    
combinations = list(itertools.product(*all_lists))
Result = []
for i in combinations:
    result1 = sum(map(lambda x:x**2, [a for a in i]))
    result2 = result1 % int(first_line[1])
    Result.append(result2)
    
print(max(Result))
