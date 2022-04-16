def solution(s):
    answer = ''
    s_list = sorted(s, reverse=True)
    answer = "".join(s_list)
    return answer