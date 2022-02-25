import sys

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
interval_sum = 0
answer = sys.maxsize
while True:
    if interval_sum >= s:
        answer = min(answer, end - start)
        interval_sum -= numbers[start]
        start += 1
    elif end == n:
        break
    else:
        interval_sum += numbers[end]
        end += 1

if answer == sys.maxsize:
    print(0)
else:
    print(answer)