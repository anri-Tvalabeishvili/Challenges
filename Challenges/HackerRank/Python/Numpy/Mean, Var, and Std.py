import numpy as np


N,M = list(map(int,input().split()))

matrix = []

for i in range(N):
    arr = matrix.append(np.array(list(map(int,input().split()))))

 

print(np.mean(matrix, axis = 1))
print(np.var(matrix, axis = 0))
print(round(np.std(matrix),11))
