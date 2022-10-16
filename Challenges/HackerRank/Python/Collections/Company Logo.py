#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__': 
    letters = sorted(input())
    letters_counter = Counter(letters).most_common()
    
    for i in range(0, 3):
        print(letters_counter[i][0], letters_counter[i][1])
