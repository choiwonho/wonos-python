def solution(s):
    answer = ''

    s = s.split(" ")
    s = list(map(int, s))

    min_value = min(s)
    max_value = max(s)

    answer = f"{min_value} {max_value}"

    return answer