import sys

si = sys.stdin.readline
n = int(si())
arr = list(map(int, si().split()))
x = int(si())
answer, cnt = 0, 0


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for i in arr:
    if gcd(x, i) == 1:
        answer += i
        cnt += 1

print(answer / cnt)
