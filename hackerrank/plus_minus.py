#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_num = 0
    negative_num = 0
    zero_num = 0
    total_len = len(arr)
    for i in arr:
        if i > 0:
            positive_num += 1
        elif i < 0:
            negative_num += 1
        else:
            zero_num += 1
    print(round(positive_num / total_len , 6))
    print(round(negative_num / total_len, 6))
    print(round(zero_num / total_len, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
