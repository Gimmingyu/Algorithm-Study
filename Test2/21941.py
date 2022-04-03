import sys
from math import inf


si = sys.stdin.readline
sys.setrecursionlimit(10**8)


def MSIS():
    return map(str, si().split())


s = si().rstrip()
m = int(si())

table = []
score = [-1 for _ in range(len(s))]
for _ in range(m):
    temp = list(MSIS())
    table.append([temp[0], int(temp[1])])


def solution(start):
    global score
    # 문자열 s의 길이를 초과하면 얻는 점수 0
    if start >= len(s):
        return 0
    # 이미 갱신된 적이 있다면 리턴해준다.
    if score[start] != -1:
        return score[start]
    # start번째의 점수는 start + 1번째의 함수가 가질 수 있는 점수 + start번째를 삭제하는 점수
    score[start] = solution(start + 1) + 1
    # key value를 받아온다.
    for k, v in table:
        # print(f"start = {start}, k = {k}, v = {v}")
        # s의 start번째에서 k가 발견되면
        if s[start:start + len(k)] == k:
            # score의 start번째에서 얻을수 있는 점수를 구해낸다.
            # 원래 점수와 k번째 문자열로 점수를 얻었을 때를 비교
            score[start] = max(score[start], solution(start + len(k)) + v)
            # print(f"start = {start}, score is now {score}")

    return score[start]


print(solution(0))
