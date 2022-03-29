import sys

si = sys.stdin.readline

n, x = map(int, si().split())
arr = list(map(int, si().split()))

if max(arr) == 0:
    print("SAD")
else:
    _max = sum(arr[:x])
    answer, cnt = _max, 1
    for i in range(x, n):
        _max = _max + arr[i] - arr[i - x]
        if _max > answer:
            answer = _max
            cnt = 1
        elif _max == answer:
            cnt += 1
    print(answer)
    print(cnt)
