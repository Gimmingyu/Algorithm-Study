from collections import deque
import sys, heapq

si = sys.stdin.readline
INF = sys.maxsize
n = int(si())
m = int(si())

# (연결된 도시, 거리) 저장해줄 리스트
link = [[] for _ in range(n + 1)]
# (각 도시까지의 최단 거리 저장해줄 리스트)
dist = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, si().split())
    link[a].append((b, c))

start, end = map(int, si().split())


def dijkstra(s):
    global link, dist
    q = []
    heapq.heappush(q, (start, 0))
    dist[start] = 0

    while q:
        now, di = heapq.heappop(q)
        if dist[now] < di:
            continue
        for town in link[now]:
            cost = di + town[1]
            if cost < dist[town[0]]:
                heapq.heappush(q, (town[0], cost))
                dist[town[0]] = cost


dijkstra(start)
print(dist[end])

