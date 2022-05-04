def solution(phone_number):
    answer = ''

    stop_len = len(phone_number) - 4
    answer = '*' * stop_len
    answer += phone_number[stop_len:]

    return answer