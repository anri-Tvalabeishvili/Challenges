# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
 
variable = input().split()

word = variable[0]

size = int(variable[1])


answer = list(permutations(word,size))

str_answer = [''.join(i) for i in answer]
str_answer.sort()

print(*str_answer, sep = "\n")
