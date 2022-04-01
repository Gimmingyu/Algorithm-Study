from collections import defaultdict
import sys
import heapq

si = sys.stdin.readline
def MIIS(): return map(int, si().split())


n = int(si())

min_heap = []
max_heap = []
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
        heapq.heappush(min_heap, (difficulty, num))
        heapq.heappush(max_heap, (-difficulty, -num))
    elif line[1] == 'solved':
        pass
    else:
        pass

print(min_heap, max_heap)
