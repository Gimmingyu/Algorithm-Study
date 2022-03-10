from collections import deque
import sys

# n을 입력 받는다
n = int(sys.stdin.readline())

# 각자의 연결된 노드를 저장해줄 리스트
graph = [[] for _ in range(n + 1)]

# bfs 사용할 큐
Queue = deque()

# 연결된 노드 정보를 입력 받는다.
for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    # 각자 연결된 노드리스트에 저장
    graph[x].append(y)
    graph[y].append(x)

# root부터 큐에 넣는다.
Queue.append(1)

# 정답 저장해줄 리스트
answer = [0] * (n + 1)


# 1과 연결된 노드부터 보기 때문에 너비우선탐색.
def bfs(q):
    global answer
    # 큐를 돌면서
    while q:
        # 노드를 하나씩 꺼낸다.
        node = q.popleft()
        # 1과 연결된 노드들을 보면서
        for num in graph[node]:
            # 아직 부모노드를 찾지 못했다면 갱신해준다.
            if not answer[num]:
                answer[num] = node
                q.append(num)
                # num과 연결된 노드들의 부모를 찾는다.

    for ans in answer[2:]:
        yield ans


for j in bfs(Queue):
    print(j)
