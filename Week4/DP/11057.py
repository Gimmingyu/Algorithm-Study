import sys

si = sys.stdin.readline
MOD = 10007
n = int(si())

table = [[0 for _ in range(10)] for _ in range(n + 1)]

# n이 1일 때 만들 수 있는 경우의 수는 자기자신뿐임
for i in range(10):
    table[1][i] = 1

# 2부터 n까지
for j in range(2, n + 1):
    # 0 부터 9 까지
    for k in range(10):
        # 자기자신부터 9까지
        for m in range(k, 10):
            table[j][k] += table[j - 1][m]

print(sum(table[n]) % MOD)
