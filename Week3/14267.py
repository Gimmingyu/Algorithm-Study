import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

# 각 노드의 부하직원을 리스트로 저장
subordinate = [[] for _ in range(n + 1)]
for i in range(1, n):
    subordinate[tree[i]].append(i + 1)
# 칭찬수치 저장할 리스트
compliment = [0] * (n + 1)

# 10**5로는 recursion error
sys.setrecursionlimit(10 ** 6)


# 깊이탐색
# 칭찬을 받은 직원의 부하리스트를 돌면서 깊이탐색 수행.
# compliment[x] = compliment[x](원래 받은 칭찬) + compliment[x-1] + w[x-1](상사가 받은 칭찬)
def dfs(nd, w):
    global compliment
    for emp in subordinate[nd]:
        compliment[emp] = dfs(emp, compliment[nd] + w)
    return compliment[nd] + w


for j in range(m):
    node, weight = map(int, sys.stdin.readline().split())
    compliment[node] += weight

dfs(1, 0)

# bfs 이용한 풀이
# que = deque()
#
#
# def sol(q):
#     global compliment
#     # (2, 2)부터 시작.
#     while q:
#         # 시작 노드와 수치 받음.
#         nd, w = q.popleft()  # 2, 2
#         compliment[nd] += w
#         for sub in subordinate[nd]:
#             q.append([sub, w])
# for _ in range(m):
#     node, weight = map(int, sys.stdin.readline().split())
#     que.append([node, weight])
#
# sol(que)

for ans in compliment[1:]:
    print(ans, end=" ")
