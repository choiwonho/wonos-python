#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the organizingContainers function below.
'''
data (2차원 배열) Input
1 1
1 1
'''


def organizingContainers(container):
    list1 = [sum(row) for row in container]  # Output > row(행)의 sum / [2, 2]
    list2 = [0] * len(container[0])  # Output > col의 sum 계산을 위한 초기화 [0, 0]

    print(container)  # Output > [[1, 1], [1, 1]]
    for j in range(len(container[0])):  # col 길이
        for i in range(len(container)):  # row 길이
            # col(열)의 sum  | ex)   list2[0] = container[0][0] + container[1][0]
            list2[j] += container[i][j]
            print(list2)  # Output > [2, 2]

    return 'Possible' if Counter(list1) == Counter(list2) else 'Impossible'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()