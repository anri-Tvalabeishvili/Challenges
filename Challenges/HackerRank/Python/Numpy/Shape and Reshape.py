import numpy

arr = input().split()
arr = list(map(int,arr))

new_array = numpy.array(arr)

print (numpy.reshape(new_array,(3,3)))

