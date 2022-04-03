import sys
from collections import defaultdict
from heapq import heappop, heappush

si = sys.stdin.readline


def MIIS(): return map(int, si().split())
def MSIS(): return map(str, si().split())


max_heap = []
min_heap = []
# recommend3 용
minmax_heap = []
maxmin_heap = []
ret = []
visited = defaultdict()
n = int(si())
for _ in range(n):
    prob, level, group = MIIS()
    heappush(max_heap, (-level, -prob, group))
    heappush(min_heap, (level, prob, group))
    heappush(maxmin_heap, (-level, prob, group))
    heappush(minmax_heap, (level, -prob, group))
    visited[prob] = False
m = int(si())
for _ in range(m):
    line = si().split()
    # print(f"command = {line}")
    if line[0] == 'recommend':
        temp = []
        if line[2] == '1':
            while max_heap and visited[-(max_heap[0][1])]:
                heappop(max_heap)
            while max_heap and max_heap[0][2] != int(line[1]):
                temp.append(heappop(max_heap))
            if max_heap:
                ret.append(-max_heap[0][1])
            else:
                ret.append(-1)
            while temp:
                heappush(max_heap, temp.pop())
        else:
            while min_heap and visited[min_heap[0][1]]:
                heappop(min_heap)
            while min_heap and min_heap[0][2] != int(line[1]):
                temp.append(heappop(min_heap))
            if min_heap:
                ret.append(min_heap[0][1])
            else:
                ret.append(-1)
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
            # 난이도 l보다 크거나 같은 문제 중 가장 쉬운 문제, 문제 번호가 작은 순
            # -level, prob, g
            while visited[maxmin_heap[0][1]]:
                heappop(maxmin_heap)
            while maxmin_heap and -(maxmin_heap[0][0]) >= int(line[2]):
                temp.append(heappop(maxmin_heap))
            if temp:
                ret.append(temp[-1][1])
            else:
                ret.append(-1)
            while temp:
                heappush(maxmin_heap, temp.pop())
        else:
            # 난이도 l보다 작은 문제 중 가장 어려운 문제, 문제 번호가 큰 순
            # level, -prob, g
            while visited[-(minmax_heap[0][1])]:
                heappop(minmax_heap)
            while minmax_heap and minmax_heap[0][0] < int(line[2]):
                temp.append(heappop(minmax_heap))
            if temp:
                ret.append(-(temp[-1][1]))
            else:
                ret.append(-1)
            while temp:
                heappush(minmax_heap, temp.pop())
    elif line[0] == 'solved':
        visited[int(line[1])] = True
    else:
        p, l, g = map(int, line[1:])
        while visited[min_heap[0][1]]:
            heappop(min_heap)
        while visited[-max_heap[0][1]]:
            heappop(max_heap)
        while visited[maxmin_heap[0][1]]:
            heappop(maxmin_heap)
        while visited[-minmax_heap[0][1]]:
            heappop(minmax_heap)
        heappush(min_heap, (l, p, g))
        heappush(max_heap, (-l, -p, g))
        heappush(minmax_heap, (l, -p, g))
        heappush(maxmin_heap, (-l, p, g))
        visited[p] = False
    # print(f"ret = {ret}")

for r in ret:
    print(r, end=" ")