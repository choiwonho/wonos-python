import re
from collections import Counter


def solution(s):
    s = Counter(re.findall('\d+', s))

    temp_arr = sorted(s.items(), key=lambda key: key[1], reverse=True)

    print(temp_arr)

    answer = list(map(int, [k for k, v in temp_arr]))

    return answer