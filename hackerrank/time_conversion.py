#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    stand = 12
    tmp_str = int(s[:2])

    if(s[-2:] == "PM"):
        if(tmp_str == stand): return s[:-2]
        tmp_str = stand + tmp_str

        result = str(tmp_str) + s[2:-2]

        return result
    else:
        if(tmp_str == stand):
            tmp_str = "00"
            result = str(tmp_str) + s[2:-2]
            return result
        else:
            return s[:-2]

if __name__ == '__main__':
    s = "06:05:45AM"
    result = timeConversion(s)
    print (result)