from itertools import permutations


def solution(numbers):
    answer = []
    nPr = permutations(numbers, 2)

    for i in list(nPr):
        if sum(i) in answer:
            continue
        answer.append(sum(i))
    return sorted(answer)