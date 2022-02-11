import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
lst = sorted(a)
answer = []

for j in a:
    for i in range(N):
        if lst[i] == j:
            print(i, end=" ")
            lst[i] = -1
            break
