from collections import deque
import sys

si = sys.stdin.readline
# 작업의 개수
n = int(si())
# 해당작업을 선행작업으로 가지는 리스트
graph = [[] for _ in range(n + 1)]
# 작업당 수행시간
time = [0] * (n + 1)
# 진입차수
entry = [0] * (n + 1)
# 각 작업까지 걸리는 시간
result = [0] * (n + 1)

for i in range(1, n + 1):
    line = list(map(int, si().split()))
    # 부모노드에 자식노드 추가
    for node in line[2:]:
        graph[node].append(i)
    # 소요시간 저장
    time[i] += line[0]
    # 진입차수 저장
    entry[i] += line[1]

q = deque()

for j in range(1, n + 1):
    if entry[j] == 0:
        result[j] += time[j]
        q.append(j)

while q:
    now = q.popleft()
    for n in graph[now]:
        entry[n] -= 1
        result[n] = max(result[n], result[now] + time[n])
        if entry[n] == 0:
            q.append(n)

print(max(result))
