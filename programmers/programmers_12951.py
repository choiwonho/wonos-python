def solution(s):
    answer = ''
    s_list = s.split(" ")

    for i in range(len(s_list)):
        s_list[i] = s_list[i][:1].upper() + s_list[i][1:].lower()

    return ' '.join(s_list)