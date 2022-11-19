import numpy as np

N,M = list(map(int,input().split()))

matrix = []

for i in range(N):
   axis = np.array(list(map(int,input().split())))
   
   matrix.append(axis)
   
matrix = np.array(matrix)

matrix = (np.sum(matrix, axis = 0))
print(np.prod(matrix))