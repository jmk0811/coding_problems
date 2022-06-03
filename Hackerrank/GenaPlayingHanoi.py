#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

def isValid(posts, disc, start, end):
    # print("{}, {}, {}".format(disc, start, end))   
    if disc > 0: # except the smallest disc
        for i in range(disc - 1, -1, -1):
            if posts[disc] == posts[i]:
                # smaller disc is present above the target disc
                # print("NOT VALID 1")
                return False
            if posts[i] == end:
                # smaller disc is present at the target post
                # print("NOT VALID 2")
                return False
    return True
    
def move(posts, disc, end):
    posts[disc] = end
    
def hanoi(posts):
    postsInt = sum(e * 10 ** i for i, e in enumerate(posts[::-1]))
    initState = postsInt
    visited = []
    prev = {}
    queue = []
    
    visited.append(postsInt)
    queue.append(postsInt)
    
    while len(queue) != 0:
        postsInt = queue.pop(0)
        posts = [int(x) for x in str(postsInt)]
        for i in range(len(posts)):
            for j in range(1, 5):
                if posts[i] != j and isValid(posts, i, posts[i], j):
                    next = copy.deepcopy(posts)
                    move(next, i, j)
                    nextPostsInt = sum(e * 10 ** i for i, e in enumerate(next[::-1]))
                    if nextPostsInt not in visited:
                        visited.append(nextPostsInt)
                        prev[nextPostsInt] = postsInt
                        queue.append(nextPostsInt)
    
    ans = []
    for i in range(len(posts)):
        ans.append(1)
    
    curr = prev[sum(e * 10 ** i for i, e in enumerate(ans[::-1]))]
    cnt = 1
    while curr != initState:
        curr = prev[curr]
        cnt += 1
    
    return cnt
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = hanoi(loc)

    fptr.write(str(res) + '\n')

    fptr.close()
