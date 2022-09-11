# Enter your code here. Read input from STDIN. Print output to STDOUT
M =  input()
A = set(input().split())
N =  input()
B = set(input().split())


B_NoT_In_A = list(map(int,B.difference(A)))
A_NoT_In_B = list(map(int,A.difference(B)))

all_numbers =  (A_NoT_In_B + B_NoT_In_A)
all_numbers.sort()

for i in all_numbers:
    print (i)