import sys

si = sys.stdin.readline
n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
go_up = [[-sys.maxsize] * m for _ in range(n)]
go_down = [[-sys.maxsize] * m for _ in range(n)]


def flight():
    sx, sy = n - 1, 0
    ex, ey = n - 1, m - 1
    up = [(1, 0), (0, -1)]
    down = [(1, 0), (0, 1)]
    go_up[sx][sy] = graph[sx][sy]
    go_down[ex][ey] = graph[ex][ey]
    # 상승 비행
    # 한 행씩 올라가면서
    for r in range(sx, -1, -1):  # 2, 1, 0
        # 오른쪽으로 탐색.
        for c in range(0, m):  # 0, 1, 2, 3
            for nx, ny in up:
                tx, ty = r + nx, c + ny
                if 0 <= tx < n and 0 <= ty < m:
                    go_up[r][c] = max(go_up[r][c], graph[r][c] + go_up[tx][ty])
    for r in range(ex, -1, -1):  # 2 1 0
        for c in range(ey, -1, -1):  # 3 2 1 0
            for nx, ny in down:
                tx, ty = r + nx, c + ny
                if 0 <= tx < n and 0 <= ty < m:
                    go_down[r][c] = max(go_down[r][c], go_down[tx][ty] + graph[r][c])

    ans = [[c + d for c, d in zip(a, b)] for a, b in zip(go_down, go_up)]
    _max = -sys.maxsize
    for i in ans:
        if max(i) > _max:
            _max = max(i)
    return _max


answer = flight()
print(answer)
