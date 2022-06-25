from collections import Counter


def solution(N, stages):
    stages_count = Counter(stages)
    people = len(stages)
    answer = []
    fail_list = {}

    for i in range(1, N + 1):
        if people != 0:
            fail_list[i] = stages_count[i] / people
            people = people - stages_count[i]
        else:
            fail_list[i] = 0

    fail_list = sorted(fail_list.items(), key=lambda item: item[1], reverse=True)

    for key in fail_list:
        answer.append(key[0])
    return answer