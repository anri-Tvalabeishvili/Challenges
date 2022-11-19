import numpy as np


N = int(input())

matrix = []

for i in range(N):
    arr = matrix.append(np.array(list(map(float,input().split()))))
    
matrix = np.array(matrix)

print(round(np.linalg.det(matrix),2))
