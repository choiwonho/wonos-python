def solution(a, b):
    answer = 0
    num_list = []
    num_list.append(a)
    num_list.append(b)
    num_list = sorted(num_list)
    for i in range(num_list[0], num_list[1] + 1):
        answer += i

    return answer