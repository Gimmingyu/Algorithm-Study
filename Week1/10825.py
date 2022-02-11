import sys

N = int(sys.stdin.readline())
score = {}

for i in range(N):
    temp = sys.stdin.readline().split()
    score[temp[0]] = [int(i) for i in temp[1:]]

answer = sorted(score.keys(), key=lambda x: (-score[x][0], score[x][1], -score[x][2], x))

for i in answer:
    print(i)
