# -*- coding: utf-8 -*-

import sys

si = sys.stdin.readline


def dp(n, files):
    # i부터 j까지의 합을 저장해줄 리스트
    s = [0]
    # dp table
    d = [[0] * n for _ in range(n)]
    # 크누스 알고리즘 적용
    a = [[0] * n for _ in range(n)]
    for m in range(n):
        # m부터 m까지의 합은 자기 자신
        a[m][m] = m
        s.append(s[m] + files[m])
    # z는 1에서 3까지 순회
    for z in range(1, n):
        # i는 0에서 (3까지, 2까지, 1까지)
        for i in range(n - z):
            # j = (1, 2, 3), (2, 3), (3)
            j = z + i  # 행 별로 now까지의 최소비용을 계산해줘야 한다.
            d[i][j] = sys.maxsize  # 우선 최대값으로 갱신해둔다.
            for k in range(a[i][j - 1], min(a[i + 1][j] + 1, j)):
                minimum = d[i][k] + d[k + 1][j] + s[j + 1] - s[i]
                if d[i][j] > minimum:
                    d[i][j] = minimum
                    a[i][j] = k
    return d[0][n - 1]


T = int(si())
answer = []

for _ in range(T):
    N = int(si())
    file = list(map(int, si().split()))
    answer.append(dp(N, file))

for ans in answer:
    print(ans)
