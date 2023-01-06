#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    
    for element in arr:
        if element < 0:
            negative += 1
        elif element > 0:
            positive += 1
        else: 
            zero+=1
    
    length = positive + negative + zero
    print(round(positive/length,6))
    print(round(negative/length,6))
    print(round(zero/length,6))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
