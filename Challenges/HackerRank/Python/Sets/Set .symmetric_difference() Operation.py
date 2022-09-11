# Enter your code here. Read input from STDIN. Print output to STDOUT
Num_1 = int(input())
abundance_A = set(input().split())
Num_2 = int(input())
abundance_B = set(input().split())


union = abundance_A.symmetric_difference(abundance_B)

print(len(union))