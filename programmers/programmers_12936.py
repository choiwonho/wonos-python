import math

def solution(n, k):
    answer = []
    n_list = list(map(int, range(1, n + 1)))

    while (n != 0):
        temp = math.factorial(n) // n  # 한개에 몇개씩의 값이 있을지 알 수 잇음.
        index = k // temp
        k = k % temp

        if k == 0:
            answer.append(n_list.pop(index - 1))
        else:
            answer.append(n_list.pop(index))
        print(answer)
        n -= 1

    return answer