from collections import deque
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
visited = [[0] * m for _ in range(n)]


queue = deque()

graph = []
for i in range(n):
    line = list(map(int, si().split()))
    for j in range(m):
        if line[j] == 9:
            queue.append((i, j))
            visited[i][j] = 1
    graph.append(line)


def bfs(g, q):
    xd = [-1, 1, 0, 0]
    yd = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = xd[idx], yd[idx]
            r, c = x + nx, y + ny
            while 0 <= r < n and 0 <= c < m:
                visited[r][c] = 1
                if g[r][c] == 9:
                    break
                if g[r][c] == 3:
                    nx, ny = -ny, -nx
                elif g[r][c] == 4:
                    nx, ny = ny, nx
                elif (g[r][c] == 1 and nx == 0) or (g[r][c] == 2 and ny == 0):
                    break
                r += nx
                c += ny
    answer = 0
    for ans in visited:
        answer += ans.count(1)
    return answer


print(bfs(graph, queue))