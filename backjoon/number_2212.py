import sys

n = input()
k = input()

# 집중국의 개수가 n 이상일떄
if k > n:
    print(0) # 각 센서의 위치에 설치하면 되므로 정답은 0
    sys.exit()

# 모든 센서의 위치를 입력받아 오름차순 정렬
array = list(map(int, input().split()))
array.sort()

# 각 센서간의 거리를 계산하여 내림차순 정렬
distance = []
for i in range(1, n):
    distance.append(array[i] - array[i - 1])

distance.sort(reverse=True)

# 가장 긴 거리부터 하나씩 제거
for i in range(k - 1):
    distance[i] = 0
print(sum(distance))