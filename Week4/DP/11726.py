import sys

si = sys.stdin.readline
n = int(si())
table = [0] * (n + 1)

table[1] = 1
table[2] = 2
for i in range(3, n + 1):
    table[i] = table[i - 1] + table[i - 2]

print(table[n] % 10007)
