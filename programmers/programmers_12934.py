def solution(n):
    answer = 0
    sqrt_val = n ** 0.5

    if sqrt_val == int(sqrt_val):
        answer = (sqrt_val + 1) ** 2
    else:
        answer = -1
    return answer