#John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, #determine how many pairs of socks with matching colors there are.

#output format 
#Return the total number of matching pairs of socks that John can sell.

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below. 

def sockMerchant(n, ar):
    counter = 0
    iterate = {}
    for i in ar:
        iterate[i]= 0
        for j in ar:
            if i==j:
                iterate[i]+=1
    for val in iterate.values():
            counter+=int(val/2)

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

