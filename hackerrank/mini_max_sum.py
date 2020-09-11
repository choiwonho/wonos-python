#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sort_arr = sorted(arr)
    result_arr = []
    min_sum = 0
    max_sum = 0

    for min_i in range(0, len(sort_arr) - 1):
        min_sum += sort_arr[min_i]
    result_arr.append(min_sum)
    for max_i in range(1, len(sort_arr)):
        max_sum += sort_arr[max_i]
    result_arr.append(max_sum)

    for result in result_arr:
        print(result, end=" ")
    return result_arr


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)