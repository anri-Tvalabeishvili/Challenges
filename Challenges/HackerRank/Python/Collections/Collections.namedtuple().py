# Enter your code here. Read input from STDIN. Print output to STDOUT
N, headers, marks = int(input()), list(input().split()), 0

for i in range(N):
    marks += int(list(input().split())[headers.index('MARKS')])
print(marks/N)

