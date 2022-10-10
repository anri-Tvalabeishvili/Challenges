# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

number_of_shoes = int(input())
shoe_sizes = dict(Counter(list(map(str,input().split()))))
number_of_customers = int(input())

income = 0

for i in range(number_of_customers):
    costumer = input().split()
    size = costumer[0]
    price = costumer[1]
    
    if size in shoe_sizes and shoe_sizes[size] > 0:
         income += int(price)
         shoe_sizes[size] = int(shoe_sizes[size]) - 1
         
        
print(income)