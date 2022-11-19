import numpy as np 

np.set_printoptions(sign=' ')
a = np.array(input().split(),float)

print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))