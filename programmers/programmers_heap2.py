import heapq


def solution(jobs):
    answer, total_time = 0, 0
    new = len(jobs)
    jobs.sort()
    while jobs:
        if total_time >= jobs[0][0]:
            tmp_queue = sorted(list(filter(lambda x: x if x[0] <= total_time else False, jobs)), key=lambda x: x[1])

            tmp_list = heapq.heappop(tmp_queue)

            # print(tp)
            total_time += tmp_list[1]
            answer += total_time - tmp_list[0]
            # print(tmp_queue)
            jobs = tmp_queue + jobs[len(tmp_queue) + 1:]
            # print(jobs)
        else:
            total_time = jobs[0][0]

    return int(answer / new)


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    result = solution(jobs)
    print(result)