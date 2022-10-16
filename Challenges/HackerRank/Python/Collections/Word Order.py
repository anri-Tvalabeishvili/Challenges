# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

words = []

for i in range(int(input())):
    word = str(input())
    words.append(word)
   
counted =  Counter(words)

print(len(set(words))) 
print(" ".join(map(str, counted.values())))

