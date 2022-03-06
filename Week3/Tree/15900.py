import sys

# 입력 받기
n = int(sys.stdin.readline())
# 연결 노드 탐색을 위한 트리
tree = [[] for _ in range(n + 1)]

# 각 노드의 부모 입력해줄 리스트
parent = [0] * (n + 1)

# 정답
answer = 0

# n-1개 줄의 입력.
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# 1. 트리의 구조를 파악한 다음, 모든 리프노드에서 루트노드까지의 거리를 계산.
# 1-1. 루트노드부터 깊이 탐색 수행해서 계산?
# 2. 수가 짝수면 선이 진다. 홀수이면 선이 이긴다.
root = 1


def dfs(node, dep):
    global tree, parent, answer
    # 연결 노드 리스트의 길이가 1이라면 리프노드에 해당하므로
    if len(tree[node]) == 1 and node != root:
        answer += dep
        return
    # 현재 노드와 연결된 노드를 탐색
    for j in tree[node]:
        # 1은 부모노드를 저장해줄 필요가 없으므로 continue
        if j == root:
            continue
        # 부모노드가 없다면 현재 노드로 저장해준다.
        if not parent[j]:
            parent[j] = node
            # 깊이를 1 증가시키면서 연결된 노드를 살핀다.
            dfs(j, dep + 1)


sys.setrecursionlimit(10**5)
dfs(1, 0)

if answer % 2 == 0:
    print("No")
else:
    print("Yes")

