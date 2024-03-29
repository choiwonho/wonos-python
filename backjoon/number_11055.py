import copy
N = int(input())
A = list(map(int, input().split()))
dp = copy.deepcopy(A)

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
