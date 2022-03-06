from collections import deque
import sys

# 입력받기
n, m = map(int, sys.stdin.readline().split())

# 그래프 설정
# 각 학생(index) 뒤에 와야하는 학생의 번호를 받아둔다.
graph = [[] for _ in range(n + 1)]
# 각 학생 별 진입차수를 저장
entry_level = [0] * (n + 1)
queue = deque()

for i in range(m):
    front, back = map(int, sys.stdin.readline().split())
    # 각 학생이 자기 뒤에 와야하는 학생들을 리스트로 갖는다.
    graph[front].append(back)
    # 진입차수를 하나 늘려준다.
    entry_level[back] += 1

# 진입차수가 0인 학생들을 큐에 넣어준다.
for student in range(1, n + 1):
    if entry_level[student] == 0:
        queue.append(student)


def bfs(q: deque):
    while q:
        # 현재 차례인 학생
        f = q.popleft()
        yield f
        # 자기 뒤에 와야하는 학생들의 진입차수를 1개씩 감소시킨다.
        for b in graph[f]:
            entry_level[b] -= 1
            # 이 때 진입차수가 0이면 큐에 추가
            if entry_level[b] == 0:
                q.append(b)


for ans in bfs(queue):
    print(ans, end=" ")
