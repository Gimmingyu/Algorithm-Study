from collections import deque
import sys

si = sys.stdin.readline

# 건물의 개수
n = int(si())

# 건물을 짓는데 드는 시간
build_time = [0] * (n + 1)

# index번 건물을 지어야 지을 수 있는 건물이 담긴 리스트
graph = [[] for _ in range(n + 1)]

# 진입차수를 입력해줄 리스트
entry = [0] * (n + 1)

# 너비탐색 진행할 큐
q = deque()

# 각 건물과 그 선행 건물을 짓기까지 소요되는 총 시간
result = [0] * (n + 1)

# 한 줄씩 입력 받아서 리스트에 담는다.
for i in range(1, n + 1):
    line = list(map(int, si().split()))
    # 건설시간 입력
    build_time[i] += line[0]
    for j in line[1:-1]:
        # 부모노드에 자식노드 추가
        graph[j].append(i)
        # 진입차수 증가
        entry[i] += 1

# 진입차수가 0인 건물들 큐에 넣고, 시간입력해준다.
for t in range(1, n + 1):
    if entry[t] == 0:
        q.append(t)
        result[t] += build_time[t]

while q:
    now = q.popleft()
    # 자식노드들
    for b in graph[now]:
        # 진입차수 감소
        entry[b] -= 1
        # 각 건물을 짓는데 걸리는 시간 갱신
        result[b] = max(result[b], result[now] + build_time[b])
        # 진입차수가 0이되면 큐에 넣는다.
        if entry[b] == 0:
            q.append(b)

for ans in result[1:]:
    print(ans)


