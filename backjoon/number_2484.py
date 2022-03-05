'''
같은 눈이 4개가 나오면 50,000원+(같은 눈)×5,000원의 상금을 받게 된다.
같은 눈이 3개만 나오면 10,000원+(3개가 나온 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개씩 두 쌍이 나오는 경우에는 2,000원+(2개가 나온 눈)×500원+(또 다른 2개가 나온 눈)×500원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
'''


def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1: # 같은 눈 4개
        return lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]: # 같은 눈 3개
            return 10000 + lst[1] * 1000
        else: # 같은 눈 2개씩 두 쌍
            return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3): # 같은 눈이 2개만 나오는 경우
        if lst[i] == lst[i + 1]:
            return 1000 + lst[i] * 100
    return lst[-1] * 100 # 모두 다른 눈이 나오는 경우

N = int(input())

print(max(money() for i in range(N)))