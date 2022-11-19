import numpy

dimention = tuple(map(int, input().split()))


zeros = numpy.zeros((dimention), dtype=int)

ones = numpy.ones((dimention), dtype=int)

print(zeros)
print(ones)