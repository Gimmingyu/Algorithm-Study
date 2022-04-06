from collections import deque, Counter
import sys

si = sys.stdin.readline
given = [6, 3, 1, 4, 12, 4]
_max = len(given)
idx = range(len(given))


def left(now, h):
    cnt = 0
    for l in range(now, -1, -1):
        if given[l] < h:
            break
        cnt += 1
    return cnt * h


def right(now, h):
    cnt = 0
    for r in range(now + 1, len(given)):
        if given[r] < h:
            break
        cnt += 1
    return cnt * h


for i in idx:
    height = given[i]
    temp = left(i, height) + right(i, height)
    if temp > _max:
        _max = temp

print(_max)
