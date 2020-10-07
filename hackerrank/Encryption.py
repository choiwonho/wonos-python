#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    input_word = s
    word_len = len(input_word)

    sqrt_result = math.sqrt(word_len)
    sqrt_rows = int(sqrt_result)
    if sqrt_result == sqrt_rows:
        sqrt_colums = sqrt_rows
    else:
        sqrt_colums = int(sqrt_result) + 1

    if word_len > sqrt_colums * sqrt_rows:
        sqrt_rows = sqrt_rows + 1

    temp_list = list()
    start_index = 0
    temp_sqrt_colums = sqrt_colums
    for i in range(sqrt_rows):
        temp_list.append(input_word[start_index:temp_sqrt_colums])
        start_index = temp_sqrt_colums
        temp_sqrt_colums += sqrt_colums

    result_list = list()
    for x in range(sqrt_colums):
        for y in range(sqrt_rows):
            try:
                result_list.append(temp_list[y][x])
            except:
                continue
        result_list.append(" ")

    final_result = ''.join(result_list)

    return final_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()