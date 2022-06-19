def solution(n, lost, reserve):
    answer = n - len(lost)
    count = 0
    reserve.sort()
    for reserve_num in reserve:
        if len(reserve) == 0 or len(lost) == 0:
            break
        elif reserve_num in lost:
            lost.remove(reserve_num)
            reserve.remove(reserve_num)
            count += 1
        else:
            plus_value = reserve_num + 1
            minus_value = reserve_num - 1
            if minus_value in lost:
                lost.remove(minus_value)
                count += 1
            elif plus_value in lost:
                lost.remove(plus_value)
                count += 1
    answer = answer + count
    print(answer)
    return answer