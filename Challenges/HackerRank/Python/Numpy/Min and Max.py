import numpy as np


N,M = list(map(int,input().split()))

minimums = []

for i in range(N):
    arr = np.array(list(map(int,input().split())))
    min_arr = minimums.append(np.min(arr))
 
    
print(np.max(minimums))