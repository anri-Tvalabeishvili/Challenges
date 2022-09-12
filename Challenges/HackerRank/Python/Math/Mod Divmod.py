# Enter your code here. Read input from STDIN. Print output to STDOUT

dividend = int(input())
divisor = int(input())

answer = divmod(dividend,divisor)

print(answer[0])
print(answer[1])
print(answer)