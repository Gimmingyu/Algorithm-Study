# K번째 수

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k

while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(1, n + 1):
        count += min(n, mid // i)
    if count >= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)
