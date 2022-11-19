import numpy as np


n, m = list(map(int, input().split()))

a = np.array([input().split() for _ in range(n)], dtype=int)
b = np.array([input().split() for _ in range(n)], dtype=int)

print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')