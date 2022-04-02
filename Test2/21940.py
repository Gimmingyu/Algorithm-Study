import sys
from heapq import heappush, heappop
from math import inf

si = sys.stdin.readline


def MIIS(): return map(int, si().split())


n, m = MIIS()

graph = [[inf] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    s, e, d = MIIS()
    graph[s][e] = d

k = int(si())
friends = list(MIIS())

# j에서 k까지 가는 시간과 i를 경유해서 가는 시간을 비교해서
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

answer = [0]
for o in range(1, n + 1):
    _max = -inf
    for f in friends:
        # 친구집이 도착지와 같으면 0이니까 패스, 친구집에서 도착지 혹은 그 반대가 경로가 없으면 패스
        if f != o and graph[f][o] != inf and graph[o][f] != inf:
            # 각 친구 집에서 목적지까지의 왕복시간이 현재 최대값보다 크면 갱신
            if _max < graph[f][o] + graph[o][f]:
                _max = graph[f][o] + graph[o][f]
    answer.append(_max)

_min = min(answer[1:])
for ans in range(1, n + 1):
    if answer[ans] == _min:
        print(ans, end=" ")
