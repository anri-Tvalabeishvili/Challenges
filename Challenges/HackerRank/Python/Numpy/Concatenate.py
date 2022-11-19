import numpy


N,M,P = input().split()

row = int(N) + int(M)

matrix = []

for i in range(row):
    arr = input().split()
    arr = list(map(int,arr))
    matrix += arr
    

print(numpy.reshape(matrix,(row,int(P))))