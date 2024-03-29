T = int(input())

def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1 # 모두 동일한 캔디를 가졌을 경우

def teacher(N, candy):
    tmp_list = [0 for i in range(N)]

    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_list[(idx + 1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += tmp_list[idx]

    return candy


def process():
    N, candy = int(input()), list(map(int, input().split()))
    count = 0
    while not check(N, candy):
        count += 1
        candy = teacher(N, candy)

    print(count)


for i in range(T):
    process()