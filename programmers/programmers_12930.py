def solution(s):
    answer = ''
    index = 0

    for word in s:
        if word == " ":
            answer += " "
            index = 0
        elif index == 0 or index % 2 == 0:
            answer += word.upper()
            index += 1
        else:
            answer += word.lower()
            index += 1

    return answer