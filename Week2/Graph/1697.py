from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001
visited[n] = 0


def bfs():
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            break

        if now - 1 >= 0 and visited[now - 1] == 0:
            q.append(now - 1)
            visited[now - 1] = visited[now] + 1
        if now + 1 <= 100000 and visited[now + 1] == 0:
            q.append(now + 1)
            visited[now + 1] = visited[now] + 1
        if now * 2 <= 100000 and visited[now * 2] == 0:
            q.append(now * 2)
            visited[now * 2] = visited[now] + 1


bfs()
print(visited[k])
