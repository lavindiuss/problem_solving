#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#For example, the square matrix arr is shown below:

#1 2 3
#4 5 6
#9 8 9  

#Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

import math
import os
import random
import re
import sys


def diagonalDifference(arr,size):

    s1 = 0
    s2 = 0
    for i in range(size):
        s1 += arr[i][i]
        s2 += arr[-i-1][i]
    return abs(s1-s2)            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()

