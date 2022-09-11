n,m = input().split()
integers = input().split()
A = set(input().split())
B = set(input().split())

happiness  = 0

for i in integers:
    if i in A:
        happiness +=1
    elif i in B:
        happiness -=1

print(happiness)
