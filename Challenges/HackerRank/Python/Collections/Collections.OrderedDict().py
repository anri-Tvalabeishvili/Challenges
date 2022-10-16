# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

ordered_dictionary = OrderedDict()

for i in range(int(input())):
    input_var = input().split()
    name = " ".join(input_var[0:-1])
    quantity = int(input_var[-1])
    ordered_dictionary[name] = ordered_dictionary.get(name,0) + quantity
    

for item in ordered_dictionary:
    print(item, ordered_dictionary.get(item))