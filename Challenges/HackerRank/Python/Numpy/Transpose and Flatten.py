import numpy

NM = input().split()
matrix = []
for i in range(int(NM[0])):
    arr = input().split()
    arr_int = list(map(int, arr))
    matrix.append(arr_int)
    

my_array = numpy.array(matrix)

print(numpy.transpose(my_array))
print(my_array.flatten())