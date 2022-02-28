from collections import deque
import sys


# 바이러스 확산시킬 함수
def spread(g):
    q = deque()
    meta = g[:]
    for virus in range(len(meta)):
        if meta[virus] == 2:
            q.append(virus)

    while q:
        x = q.popleft()
        for next_to in link[x]:
            if meta[next_to] == 0:
                meta[next_to] = 2
                q.append(next_to)

        # for d in direction:
        #     tmp = x + d
        #     if (0 <= x < n * m) and (0 != x % m != m - 1) and meta[tmp] == 0:
        #         meta[tmp] = 2
        #         q.append(tmp)

    global answer
    now = meta.count(0)
    answer = max(answer, now)


def make_wall(count):
    if count == 3:
        spread(graph)
        return
    for tile in range(len(graph)):
        if graph[tile] == 0:
            graph[tile] = 1
            make_wall(count + 1)
            graph[tile] = 0


n, m = map(int, sys.stdin.readline().split())

# 맵 정보
graph = []

# 정답
answer = 0

# 인접 노드
link = [[] for k in range(n * m)]
direction = [-1, 1, -m, m]
# 입력 받기
for r in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for v in temp:
        graph.append(v)

# 인접 노드 설정
for i in range(len(graph)):
    if i % m != 0:
        link[i].append(i - 1)
    if i % m != m - 1:
        link[i].append(i + 1)
    if i > m - 1:
        link[i].append(i - m)
    if i < m * (n - 1):
        link[i].append(i + m)

make_wall(0)

print(answer)
