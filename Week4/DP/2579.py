import sys

si = sys.stdin.readline

n = int(si())
score = [0] * 301
table = [0] * 301
for i in range(1, n + 1):
    now = int(si())
    score[i] += now

table[1] = score[1]
table[2] = score[2] + score[1]
table[3] = max((score[1] + score[3]), (score[2] + score[3]))
for now in range(4, 301):
    table[now] = max(table[now - 3] + score[now - 1] + score[now], table[now - 2] + score[now])

print(table[n])
