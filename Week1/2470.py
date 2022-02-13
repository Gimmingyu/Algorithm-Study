import sys

n = int(sys.stdin.readline())
arr = sorted(map(int, sys.stdin.readline().split()))

start = 0
end = len(arr) - 1
target = [arr[0], arr[-1]]
mid = arr[0] + arr[-1]
while start != end:
    if abs(arr[start] + arr[end]) == 0:
        target = sorted([arr[start], arr[end]])
        break
    if abs(arr[start] + arr[end]) > abs(mid):
        if abs(arr[start]) < abs(arr[end]):
            end -= 1
            continue
        else:
            start += 1
            continue
    elif abs(arr[start] + arr[end]) < abs(mid):
        target = sorted([arr[start], arr[end]])
        mid = sum(target)
        if abs(arr[start]) < abs(arr[end]):
            end -= 1
            continue
        else:
            start += 1
            continue
    else:
        if abs(arr[start]) < abs(arr[end]):
            end -= 1
            continue
        else:
            start += 1
            continue

for i in target:
    print(i, end=" ")
