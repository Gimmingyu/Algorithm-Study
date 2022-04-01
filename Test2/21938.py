import sys
from collections import deque, Counter

si = sys.stdin.readline
def MIIS(): return map(int, si().split())


n, m = MIIS()
screen = [list(MIIS()) for _ in range(n)]
t = int(si())

graph = [[] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    line = screen[i]
    col = 0
    for j in range(0, (3 * m), 3):
        avg = sum(line[j:j + 3])
        if avg >= (t * 3):
            avg = 255
        else:
            avg = 0
        graph[i].append(avg)
        col += 1


def bfs(start, num):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        graph[x][y] = num
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 255 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


case = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 255:
            bfs((i, j), case)
            case -= 1


answer = min([min(arg) for arg in graph])
print(answer * - 1)
