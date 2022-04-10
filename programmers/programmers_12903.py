def solution(s):
    answer = ''
    position = len(s) // 2

    if len(s) % 2 == 0:
        answer = s[position - 1] + s[position]
    else:
        answer = s[position]

    return answer