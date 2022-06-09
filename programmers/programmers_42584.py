def solution(prices):
    answer = []
    for index in range(len(prices)):
        cnt = 0
        # basic_count = len(prices) - 1 - index
        for index2 in range(index + 1, len(prices)):
            cnt += 1
            if (prices[index] > prices[index2]):
                break

        answer.append(cnt)

    return answer