#!/bin/python3
import os


# Complete the solve function below.
def solve(s):
    Names_as_a_list = s.split(" ")
    full_name = ""
    
    for name in Names_as_a_list:
        new_name= name[:1].upper() + name[1:] + " "
        full_name += new_name
        
    return full_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
