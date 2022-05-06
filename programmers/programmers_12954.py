def solution(x, n):
    answer = []
    if x == 0:
        answer = [0] * n
        return answer;
    if x > 0:
        repeat_range = (x * n) + 1
    if x < 0:
        repeat_range = (x * n) - 1
    for i in range(x, repeat_range, x):
        answer.append(i)
    return answer