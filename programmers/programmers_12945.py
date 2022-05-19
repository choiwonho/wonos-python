def solution(n):
    pibo_list = [0, 1]

    for i in range(2, n + 1):
        pibo_list.append(pibo_list[i - 2] + pibo_list[i - 1])

    return pibo_list[-1] % 1234567