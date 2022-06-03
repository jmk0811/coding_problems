#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    dict = {}
    cnt = 0
    
    for num in s:
        rem = num % k
        if rem in dict: dict[rem] += 1
        else: dict[rem] = 1
    
    if k / 2 in dict: cnt += min(dict[k/2], 1)
    if 0 in dict: cnt += min(dict[0], 1)
    
    for i in range(1, k // 2 + 1):
        if i != k / 2 and i != k - i:
            if i in dict and k - i in dict: cnt += max(dict[i], dict[k - i])
            elif i in dict: cnt += dict[i]
            elif k - i in dict: cnt += dict[k - i]
        
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
