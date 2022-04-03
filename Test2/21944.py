import sys
from collections import defaultdict
from heapq import heappop, heappush

si = sys.stdin.readline


def MIIS(): return map(int, si().split())
def MSIS(): return map(str, si().split())


max_heap = []
min_heap = []
ret = []
visited = defaultdict()
n = int(si())
for _ in range(n):
    prob, level, group = MIIS()
    heappush(max_heap, (-level, -prob, group))
    heappush(min_heap, (level, prob, group))
    visited[prob] = False
m = int(si())
for _ in range(m):
    line = si().split()
    print(f"command = {line}")
    if line[0] == 'recommend':
        temp = []
        if line[1] == '1':
            print(f"max_heap = {max_heap[0]}")
            while visited[-(max_heap[0][1])]:
                heapq.heappop(max_heap)
            while (max_heap[0][2]) != int(line[1]):
                temp.append(heappop(max_heap))
            ret.append(-max_heap[0][1])
            while temp:
                heappush(max_heap, temp.pop())
        else:
            while visited[-(min_heap[0][1])]:
                heapq.heappop(min_heap)
            while min_heap[0][2] != int(line[1]):
                temp.append(heappop(min_heap))
            ret.append(min_heap[0][1])
            while temp:
                heappush(min_heap, temp.pop())
    elif line[0] == 'recommend2':
        if line[1] == '1':
            while visited[-(max_heap[0][1])]:
                heappop(max_heap)
            ret.append(-max_heap[0][1])
        else:
            while visited[min_heap[0][1]]:
                heappop(min_heap)
            ret.append(min_heap[0][1])
    elif line[0] == 'recommend3':
        temp = []
        if line[1] == '1':
            while visited[-(max_heap[0][1])]:
                heappop(max_heap)
            while -(max_heap[0][0]) >= int(line[2]):
                temp.append(heappop(max_heap))
            ret.append(-(temp.pop()[1]))
            while temp:
                heappush(max_heap, temp.pop())
        else:
            while visited[min_heap[0][1]]:
                heappop(min_heap)
            while min_heap[0][0] >= int(line[2]):
                temp.append(heappop(min_heap))
            ret.append(temp.pop()[1])
            while temp:
                heappush(min_heap, temp.pop())
    elif line[0] == 'solved':
        visited[int(line[1])] = True
    else:
        p, l, g = map(int, line[1:])
        while visited[min_heap[0][1]]:
            heappop(min_heap)
        while visited[-max_heap[0][1]]:
            heappop(max_heap)
        heappush(min_heap, (l, p, g))
        heappush(max_heap, (-l, -p, g))
        visited[p] = False

# recommend: 1인 경우 group에서 가장 어려운 문제, -1이면 가장 쉬운 문제
# --> max_heap에서 꺼내면서 g랑 같지 않으면 리스트에 보관, 발견하면 다시 넣기
# --> min_heap에서 꺼내면서 g랑 같지 않으면 리스트에 보관, 발견하면 다시 넣기
# recommend2: 1인 경우 group 상관없이 가장 어려운 문제, ...
# recommend3:
# 1인 경우 group 상관없이 level 이상중에 가장 쉬운 문제
# --> 문제 번호 작은 순서, 없으면 -1
# -1인 경우 group 상관없이 level 이하중에 가장 어려운 문제
# --> 문제 번호 큰 순서, 없으면 -1
