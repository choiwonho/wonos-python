import sys
input = sys.stdin.readline

#DP[i][j] : i, j에 도착했을때의 최댓값
N = int(input())
A = [[0] * (N + 1) for _ in range(N + 1)]
DP = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(1, i+1):
        A[i][j] = temp[j-1]

for i in range(1, N+1):
    for j in range(1, N+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + A[i][j]

print(max(DP[N]))