def solution(s):
    answer = True
    p_count = 0
    y_count = 0

    s = s.lower()
    for i in s:
        if i == "p":
            p_count += 1
        elif i == "y":
            y_count += 1

    if p_count != y_count:
        return False

    return True