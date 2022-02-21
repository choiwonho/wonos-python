# x번째 행에 놓은 Queen에 대한 검증
def check(x):
    # 이전 행에 놓았던 모든 Queen들을 확인
    for i in range(x):
        # 위쪽 혹은 대각선을 확인
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

# x번째 행에 대하여 처리
def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        # x 번째 행의 각 열에 Queen을 둔다고 가정
        for i in range(n):
            row[x] = i
            # 해당위치에 Queen을 두어도 괜찮은 경우
            if check(x):
                dfs(x + 1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)