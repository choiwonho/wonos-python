def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = lottos.count(0)

    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1

    answer.append(rank[zero_count + count])
    answer.append(rank[count])

    return answer