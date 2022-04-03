from collections import defaultdict
import sys
import heapq

si = sys.stdin.readline
def MIIS(): return map(int, si().split())


n = int(si())

# recommend 용
min_heap = []
max_heap = []
ret = []

visited = defaultdict()

for _ in range(n):
    num, difficulty = MIIS()
    heapq.heappush(min_heap, (difficulty, num))
    heapq.heappush(max_heap, (-difficulty, -num))
    visited[num] = False
m = int(si())
for _ in range(m):
    line = si().split()
    if line[0] == 'add':
        num, difficulty = map(int, line[1:])
        while visited[(min_heap[0][1])]:
            heapq.heappop(min_heap)
        while visited[-(max_heap[0][1])]:
            heapq.heappop(max_heap)
        heapq.heappush(min_heap, (difficulty, num))
        heapq.heappush(max_heap, (-difficulty, -num))
        visited[num] = False

    elif line[0] == 'solved':
        visited[int(line[1])] = True

    else:
        if line[1] == '1':
            while visited[-(max_heap[0][1])]:
                heapq.heappop(max_heap)
            ret.append(-max_heap[0][1])
        else:
            while visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            ret.append(min_heap[0][1])


for ans in ret:
    print(ans)
