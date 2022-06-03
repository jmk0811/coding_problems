#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    l = list(w)
    length = len(l)
    pivot = -1
    temp = l[length - 1]
    for i in range(length - 2, -1, -1):
        print(l[i])
        if temp <= l[i]: 
            temp = l[i]
            continue
        else: 
            pivot = i
            break
        
    if pivot < 0: return "no answer"
    
    for i in range(length - 1, pivot, -1):
        if l[i] > l[pivot]:
            l[i], l[pivot] = l[pivot], l[i]
            break
        
    tempList = []
    for i in range(pivot + 1, length):
        tempList.append(l[i])
    
    str = "".join(l[0:pivot + 1] + tempList[::-1])
    
    return str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
