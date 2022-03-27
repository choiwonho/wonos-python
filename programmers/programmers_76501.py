def solution(absolutes, signs):
    answer = 0

    for i in zip(absolutes, signs):
        if i[1]:
            answer += i[0]
        else:
            answer -= i[0]

    return answer