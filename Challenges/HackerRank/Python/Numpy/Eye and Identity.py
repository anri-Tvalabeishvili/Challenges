import numpy

X1, X2 = list(map(int,input().split()))

matrix = str(numpy.eye(X1, X2, k = 0))

print( matrix.replace('1',' 1').replace('0',' 0'))


