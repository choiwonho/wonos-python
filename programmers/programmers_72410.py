import re


def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id)
    answer = re.sub('\.\.+', '.', answer)
    answer = re.sub('^\.|\.$', '', answer)

    # 5
    if answer == '':
        answer = 'a'

    # 6
    answer = re.sub('\.$', '', answer[0:15])

    # 7
    while len(answer) <= 2:
        answer += answer[-1:]

    return answer