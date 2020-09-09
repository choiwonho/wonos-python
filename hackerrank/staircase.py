#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    num = n
    check_space = " "
    check_sharp = "#"
    for index, i in enumerate(range(1, n+1)):
        space = check_space * (num - i)
        sharp = check_sharp * i
        print(str(space) + str(sharp))



if __name__ == '__main__':
    n = int(input())

    staircase(n)
