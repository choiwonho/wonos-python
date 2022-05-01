def check_even(num):
    if num % 2 == 0:
        num = num // 2
    else:
        num = (num * 3) + 1

    return num


def solution(num):
    if num == 1:
        return 0
    else:
        for i in range(501):
            num = check_even(num)

            if num == 1:
                return i + 1
            if i == 500:
                return -1