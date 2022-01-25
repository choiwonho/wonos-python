
'''
N, M : 입력값

adj : 섬간 인접리스트

start_node, end_node : 공장이 위치한 섬의 번호

start, end : 이분 탐색 범위 (중량의 최솟값 ~ 중량의 최댓값)


BFS와 이분 탐색을 활용한 문제였다. 처음 접해보는 유형이었고, 새로운 방식의 아이디어 및 풀이를 얻을 수 있는 문제였다.


1. 이분 탐색을 통해 가능한 중량을 찾는다.

- BFS 탐색을 통해 start_node 섬에서 end_node 섬으로 갈 수 있는지 확인

- 갈 수 있으면 start 증가시켜 start_node에서 end_node로 갈 수 있는 최고값에 근접시키기

- 불가능하다면 end를 감소시켜 start_node에서 end_node로 갈 수 있는 값에 근접시키기



2. 1의 과정을 반복하면서 가능한 최대 중량을 탐색한다.
'''

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True

    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start
while(start <= end):
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)