from collections import deque
import sys


def move(x, y):
    if not is_visited[x][y]:
        is_visited[x][y] = True
        q.append([x, y])


def bfs():
    # x, y, z = a, b, c 에 현재 담겨있는 물
    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0 and z not in answer:
            answer.append(z)

        # x -> y
        water = min(x, b - y)
        move(x - water, y + water)
        # x -> z
        water = min(x, c - z)
        move(x - water, y)
        # y -> x
        water = min(y, a - x)
        move(x + water, y - water)
        # y -> z
        water = min(y, c - z)
        move(x, y - water)
        # z -> x
        water = min(z, a - x)
        move(x + water, y)
        # z -> y
        water = min(z, b - y)
        move(x, y + water)


a, b, c = map(int, sys.stdin.readline().split())
answer = []
# a는 계량컵, b와 c에 물을 옮겨 담는 경우의 수.
q = deque()
q.append((0, 0))

is_visited = [[False] * (b + 1) for t in range(a + 1)]
is_visited[0][0] = True

bfs()
# 정답 0출력
answer.sort()
for i in answer:
    print(i, end=" ")
