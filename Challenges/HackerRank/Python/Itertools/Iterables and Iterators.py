# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
Letters = input().split()
K = int(input())

Combinations = list(combinations(Letters, K))
Filtered = filter(lambda c: 'a' in c, Combinations)
print("{0:.3}".format(len(list(Filtered))/len(Combinations)))