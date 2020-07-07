#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_count = 0
    b_count = 0
    result = []
    for a_compare, b_compare in zip(a,b):
        if a_compare > b_compare:
            a_count += 1
        elif a_compare < b_compare:
            b_count += 1
        else:
            continue
    result.append(a_count)
    result.append(b_count)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
