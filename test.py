from heapq import heappush, heappop, heappushpop, heapreplace, merge


heap = [1, 2, 3, 4, 5]
sub = [4, 5, 6, 7, 8]
print(heappop(heap))
heap = list(merge(heap, sub))
print(heap)