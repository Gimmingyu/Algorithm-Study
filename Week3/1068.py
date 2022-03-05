from collections import deque
import sys

n = int(sys.stdin.readline())

tree = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

q = deque()

# 부모가 적힌 리스트를 돌면서, 지울 노드를 부모로 지니는 노드들을 큐에 담는다.
# 큐에 담긴 노드들을 부모로 지니는 노드들을 큐에 넣으면서, 각 노드들을 삭제(-2) 시킨다.
# 위의 결과로 나온 트리를 탐색해서 자신(인덱스)을 부모로 지니는(값)노드가 없는 노드들을 카운트한다.
for i in range(n):
    if tree[i] == target:
        # 지울 노드를 부모로 지니는 노드들을 큐에 담는다.
        q.append(i)

# 지울 노드를 -2로 갱신
tree[target] = -2
while q:
    # 지울 노드를 부모로 지니는 노드 x
    x = q.popleft()
    for node in range(n):
        # x를 부모로 지니는 노드들을 큐에 넣는다.
        if tree[node] == x:
            q.append(node)
        # x노드를 삭제한다.
        tree[x] = -2

answer = 0
for j in range(n):
    # 제거 되지 않았으면서 자식이 없는 노드의 개수.
    if j not in tree and tree[j] != -2:
        answer += 1

print(answer)
