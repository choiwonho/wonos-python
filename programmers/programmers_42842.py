def solution(brown, yellow):
    total = brown + yellow  # 전체 카펫의 칸

    for weight in range(total, 2, -1):  # 가로
        if total % weight == 0:  # 카펫넓이에서 가로길이 탐색
            height = total // weight  # 카펫넓이 / 가로길이를 통해 세로길이 탐색
            if yellow == (weight - 2) * (height - 2):
                return [i, a]