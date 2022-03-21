from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)

    call_user_list = defaultdict(set)  # 유저 A가 신고한 유저 목록(set)
    ben_user_list = defaultdict(int)  # 유저 A가 신고당한 횟수(int)
    stop = []

    for i in report:
        call_user, ben_user = i.rsplit()
        ben_user_list[ben_user] += 1
        call_user_list[call_user].add(ben_user)

        if ben_user_list[ben_user] == k:
            stop.append(ben_user)

    for s in stop:
        for i in range(len(id_list)):
            if s in call_user_list[id_list[i]]:
                answer[i] += 1

    return answer