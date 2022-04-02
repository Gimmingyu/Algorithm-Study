import sys
from collections import deque
from heapq import heappush, heappop, heapify
si = sys.stdin.readline
def MIIS(): return map(int, si().split())


n, m = MIIS()

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    b1, b2, dist = MIIS()
    graph[b1][b2] = dist

k = int(si())
friends = list(MIIS())
# 친구들의 도시를 넣고 친구가 사는 도시에서 가장 가까운 곳부터 선택.
# 돌아오는 길이 있는 경우와 없는 경우
# 모든 도시를 방문할 때까지 heapq로 꺼낸다
# 모든 도시까지의 왕복시간 최대값중 최소값을 찾는다.
# 친구들이 사는 곳 부터 모든 도시까지의 최단거리(왕복시간)를 너비탐색으로 계산.
# 도시별 왕복시간의 최대값중 최소값을 뽑는다.


def bfs(start):
    # heapq
    q = []
    # 출발 도시에서 각 도시까지의 최단거리를 저장할 테이블
    table = [0] * (n + 1)
    # 방문 리스트
    visited = set()
    visited.add(start)
    # 친구들이 사는 도시와 연결된 도시를 큐에 넣는다.
    for j in range(1, n + 1):
        if graph[start][j]:
			table[j] += graph[start][j]
            heappush(q, (graph[i][j], start, j))

    while q:
        # 출발지에서 가장 가까운 도시.
        dist, b1, b2 = heappop(q)
        # b2를 방문처리 한다.
        if b2 not in visited:
            visited.add(b2)
            # b2까지의 거리를 넣어준다.
            table[b2] += table[b1] + dist

    return table


for i in friends:
    t = dfs(i)
