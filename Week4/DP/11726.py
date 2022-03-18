import sys

si = sys.stdin.readline
n = int(si())
table = [0] * 1001

table[1] = 1
table[2] = 2
for i in range(3, 1001):
    table[i] = table[i - 2] + table[i - 1]

print(table[n] % 10007)
