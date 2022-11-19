import numpy as np


arr = np.array(list(map(float,input().split())))
value = int(input())

print(np.polyval(arr, value))