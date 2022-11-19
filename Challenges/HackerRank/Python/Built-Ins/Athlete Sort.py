#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    

counter = 0   
dictinarty = {}  
  
for i in arr:
    dictinarty[counter]  = i[k]
    counter += 1
    
dictinarty = dict(sorted(dictinarty.items(), key=lambda item: item[1]))
incexes = dictinarty.keys()

for i in incexes:
    print(*arr[i])