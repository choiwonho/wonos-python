def solution(n):
    string_val = "수박수박수"
    #list_string = list(string_val)
    answer = ''
    for i in range(n):
        if i == 0 or i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
        #answer += list_string[i]
    print(answer)
    return answer