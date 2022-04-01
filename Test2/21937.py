from collections import deque
import sys

si = sys.stdin.readline
def MIIS(): return map(int, si().split())


n, m = MIIS()
todo = [[] * (n + 1) for _ in range(n + 1)]
tree = [0] * (n + 1)
visited = [False] * (n + 1)
sys.setrecursionlimit(10 ** 6)

for _ in range(m):
    a, b = MIIS()
    todo[b].append(a)

x = int(si())


def dfs(x):
    if not todo[x]:
        visited[x] = True
        return 0
    for node in todo[x]:
        if not visited[node]:
            tree[x] += dfs(node) + 1
            visited[node] = True
    return tree[x]


print(dfs(x))
