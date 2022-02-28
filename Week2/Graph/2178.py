from collections import deque
import sys

# map
arr = []

# direction
rd = [-1, 1, 0, 0]
cd = [0, 0, -1, 1]

# input
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    a = [int(j) for j in sys.stdin.readline() if j != '\n']
    arr.append(a)


# bfs
def bfs(x, y):
    q = deque()
    q.append([y, x])

    while q:
        row, col = q.popleft()
        for d in range(4):
            nx = col + cd[d]
            ny = row + rd[d]
            # print(nx, ny)
            if nx < 0 or m <= nx or ny < 0 or n <= ny:
                continue
            if arr[ny][nx] == 0:
                continue
            if nx == 0 and ny == 0:
                continue
            if arr[ny][nx] == 1:
                arr[ny][nx] = arr[row][col] + 1
                q.append([ny, nx])
    return arr[n - 1][m - 1]


print(bfs(0, 0))
