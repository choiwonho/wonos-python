from collections import deque


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        result = ""
        bin_arr1 = deque(format(arr1[i], 'b'))
        bin_arr2 = deque(format(arr2[i], 'b'))

        if len(bin_arr1) < n:
            for j in range(n - len(bin_arr1)):
                bin_arr1.appendleft("0")
        if len(bin_arr2) < n:
            for j in range(n - len(bin_arr2)):
                bin_arr2.appendleft("0")

        for a, b in zip(bin_arr1, bin_arr2):

            if a == '1' or b == '1':
                result += "#"
            elif a == '0' and b == "0":
                result += " "

        answer.append(result)
    return answer