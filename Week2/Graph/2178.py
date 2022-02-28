from collections import deque
import sys

# map
arr = []
graph = []
# direction
# rd = [-1, 1, 0, 0]
# cd = [0, 0, -1, 1]

# input
n, m = map(int, sys.stdin.readline().split())
# for i in range(n):
#     a = [int(j) for j in sys.stdin.readline() if j != '\n']
#     arr.append(a)
for r in range(n):
    temp = sys.stdin.readline()
    for v in temp:
        if v != '\n':
            graph.append(int(v))

print(graph)
link = [[] for k in range(n * m)]
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


# bfs
# def bfs(x, y):
#     q = deque()
#     q.append([y, x])
#
#     while q:
#         row, col = q.popleft()
#         for d in range(4):
#             nx = col + cd[d]
#             ny = row + rd[d]
#             # print(nx, ny)
#             if nx < 0 or m <= nx or ny < 0 or n <= ny:
#                 continue
#             if arr[ny][nx] == 0:
#                 continue
#             if nx == 0 and ny == 0:
#                 continue
#             if arr[ny][nx] == 1:
#                 arr[ny][nx] = arr[row][col] + 1
#                 q.append([ny, nx])
#     return arr[n - 1][m - 1]


def bfs2():
    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        for node in link[now]:
            print(node)
            if graph[node] == 0:
                continue
            if graph[node] == 1:
                graph[node] = graph[now] + 1
                q.append(node)

    return graph[-1]


bfs2()

# print(bfs(0, 0))
print(graph[-1])
