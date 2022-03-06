from collections import deque
import sys

si = sys.stdin.readline

# 테스트 케이스 개수
T = int(si())

# 정답을 담을 리스트
answer = []
# 너비탐색에 사용할 큐
queue = deque()


# 선행 건물들을 입력하고 진입차수를 등록해줄 함수
# 테스트케이스만큼 반복해야해서 함수로 만들었다.
def set_testcase(time):
    for i in range(time):
        front, back = map(int, si().split())
        # front번째 건물을 지어야 back 건물을 지을 수 있다.
        graph[front].append(back)
        # back 건물의 진입차수 +1
        entry[back] += 1
    target = int(si().rstrip())
    return target


def bfs(q: deque, target):
    # 각 건물까지 소요되는 시간을 저장한다.
    result = [0] * (n + 1)
    # 진입차수가 0인 건물들을 큐에 담는다.
    for i in range(1, n + 1):
        if entry[i] == 0:
            q.append(i)
            result[i] += build_time[i]
    while q:
        # 현재 건설하는 건물
        now = q.popleft()
        # 현재 건물을 선행으로 가지는 건물들
        for b in graph[now]:
            # 각 건물들의 진입차수를 하나씩 줄여준다.
            entry[b] -= 1
            # 다음 건물들을 짓는데 걸리는 시간(이전에 입력된 수치) vs 현재 건물을 짓고 다음 건물까지 짓는 시간
            # 두 개를 비교해서 병목자원에 대한 시간만 입력해줘야한다.
            result[b] = max(result[b], result[now] + build_time[b])
            if entry[b] == 0:
                q.append(b)
    return result[target]


# 목표 건물에서 선행건물들의 시간을 더해가면서 계산한다.
# 큐 형식으로 목표 건물에서 선행건물들을 큐에 넣어가는 식.
# 선행건물의 선행건물도 큐에 넣는다.
# 차례로 올라가다 더 이상 선행건물이 없다면 answer에 시간을 담는다.
for j in range(T):
    # 건물 개수와 비교 횟수
    n, k = map(int, si().split())
    # index번째 건물 앞에 와야할 건물들이 담길 리스트
    graph = [[] for _ in range(n + 1)]
    # 진입차수가 담길 리스트
    entry = [0] * (n + 1)
    # 건물 건설시간 리스트
    build_time = [0] + list(map(int, si().split()))
    w = set_testcase(k)
    t = bfs(queue, w)
    answer.append(t)
    queue.clear()

for ans in answer:
    print(ans)
