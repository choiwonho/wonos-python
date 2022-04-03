def solution(n):
    answer = 0
    three_list = list()

    while n != 0:
        three_list.append(n % 3)
        n = int(n / 3)

        if n == 0:
            break
    pow_val = len(three_list) - 1

    for i in three_list:
        answer += i * pow(3, pow_val)
        pow_val -= 1

    return answer