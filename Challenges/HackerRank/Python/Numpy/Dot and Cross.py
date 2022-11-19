import numpy as np


N =int(input())

A = []
B = []

for i in range(N):
    arr = A.append(np.array(list(map(int,input().split()))))
    
for i in range(N):
    arr = B.append(np.array(list(map(int,input().split()))))
    
A = np.array(A)
B = np.array(B)
print(np.dot(A,B))