# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
 
range1 = [int(i) for i in input().split()]
range2 = [int(i) for i in input().split()]

union = [range1 , range2]

answer = (list(product(*union)))

print(*answer, sep = " ")
