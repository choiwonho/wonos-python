def solution(n):
    answer = sorted(list((map(str, str(n)))), reverse=True)

    return int(''.join(answer))