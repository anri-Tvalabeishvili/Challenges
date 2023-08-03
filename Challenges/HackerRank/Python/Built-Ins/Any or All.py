# Enter your code here. Read input from STDIN. Print output to STDOUT

quantity,numbers = int(input()),input().split()
print(all([int(i)>0 for i in numbers]) and any([j == j[::-1] for j in numbers]))
