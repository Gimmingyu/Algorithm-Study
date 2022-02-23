import sys
from collections import Counter

n = int(sys.stdin.readline())
counter = Counter()
for i in range(n):
    a, c, b = map(int, sys.stdin.readline().split())
    for num in range(a, c + 1, b):
        if counter[num]:
            counter[num] += 1
        else:
            counter[num] = 1

