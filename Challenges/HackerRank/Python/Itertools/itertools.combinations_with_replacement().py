# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
 
variable = input().split()

word = [i for i in variable[0]]
word.sort()

size = int(variable[1])

answer = list(combinations_with_replacement(word,size))
str_answer = [''.join(i) for i in answer]
print(*str_answer, sep = "\n")
