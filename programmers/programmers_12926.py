def solution(s, n):
    answer = ''
    upper_list = list()
    lower_list = list()

    for i in range(ord('A'), ord('Z') + 1):
        upper_list.append(chr(i))
    for i in range(ord('a'), ord('z') + 1):
        lower_list.append(chr(i))

    for i in s:
        if i in upper_list:
            next_index = upper_list.index(i) + n
            answer += upper_list[next_index % 26]
        elif i in lower_list:
            next_index = lower_list.index(i) + n
            answer += lower_list[next_index % 26]
        else:
            answer += " "

    return answer