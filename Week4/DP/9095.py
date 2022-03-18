import sys

si = sys.stdin.readline
answer = []


def end_dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4


def dp(n):
    if n <= 3:
        return end_dp(n)
    return dp(n - 1) + dp(n - 2) + dp(n - 3)


T = int(si())
for _ in range(T):
    num = int(si())
    answer.append(dp(num))

for i in answer:
    print(i)
