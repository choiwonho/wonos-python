def solution(dartResult):
    temp_answer = list()

    score_dic = {'S': 1, 'D': 2, 'T': 3}

    for i, word in enumerate(dartResult):
        answer = 0

        if word == "*":
            temp_answer[-1] = temp_answer[-1] * 2
            answer += pow(int(dartResult[i - 2]), score_dic[word]) * 2
            temp_answer.append(answer)

        elif word in score_dic:
            answer += pow(int(dartResult[i - 1]), score_dic[word])
            temp_answer.append(answer)


print(temp_answer)

return answer