import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


def plus_count(e):
    num = 0
    while num <= e:
        num += e
        e -= 1
    return num


start, end, count = 0, 0, 0
temp = [False] * 100000
while start < n:
    while end < n and not temp[arr[end]]:
        temp[arr[end]] = True
        end += 1
    count += plus_count(end - start)
    temp[arr[start]] = False
    start += 1

print(count)
