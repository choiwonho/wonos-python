import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer



if __name__ == '__main__':

    temp_scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    result = solution(temp_scoville, K)
    print(result)