#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
  
    print(format(len([x for x in arr if x>0])/len(arr),'.6f'))
    print(format(len([x for x in arr if x<0])/len(arr),'.6f'))
    print(format(len([x for x in arr if x==0])/len(arr),'.6f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

