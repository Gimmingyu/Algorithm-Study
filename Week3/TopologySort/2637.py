from collections import deque
import sys

si = sys.stdin.readline

# 완제품 번호
n = int(si())
# m개의 줄
m = int(si())
# 자식 노드 담을 리스트
graph = [[] for _ in range(n + 1)]
# 각 부품이 몇 개씩 필요한지 담을 리스트
needs = [[0] * (n + 1) for _ in range(n + 1)]
# 진입
entry = [0] * (n + 1)
for i in range(m):
    x, y, z = map(int, si().split())
    # x제품을 만드는데에 y부품이 z개 필요하다.
    graph[y].append((x, z))
    entry[x] += z

q = deque()

for k in range(1, n + 1):
    if entry[k] == 0:
        q.append(k)

while q:
    now = q.popleft()
    for nxt, weight in graph[now]:
        # 중간부품 혹은 완제품 이라면
        # 현재 제품을 만드는데 필요했던 부품들 * 해당 중간부품이 필요로 하는 현재 제품의 개수
        for w in range(1, n + 1):
            needs[nxt][w] += needs[now][w] * weight
        # 진입차수 줄여준다.
        entry[nxt] -= weight
        # 0이되면 넣어준다.
        if entry[nxt] == 0:
            q.append(nxt)
        # x 제품을 만드는데 now가 y개 필요하다.

for idx, ans in enumerate(needs[n]):
    if idx != 0 and ans != 0:
        print(idx, ans)
