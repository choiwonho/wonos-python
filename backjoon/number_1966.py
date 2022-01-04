# 문제 체크 개수
test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' '))) # 4, 2 (4개의 원소중 2번째 인덱스)
    queue = list(map(int, input().split(' '))) # [2, 1, 4, 3]
    queue = [(i, idx) for idx, i in enumerate(queue)] # [(2,0), (1,1), (4,2), (3,3)]
    count = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
