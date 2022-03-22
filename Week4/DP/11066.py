# -*- coding: utf-8 -*-

import sys

si = sys.stdin.readline

def dp(n, files):
	# i부터 j까지의 합을 저장해줄 리스트
	S = [0]
	# dp table
	D = [[0] * n for _ in range(n)]
	# 크누스 알고리즘 적용
	A = [[0] * n for _ in range(n)]
	for m in range(n):
		# m부터 m까지의 합은 자기 자신
		A[m][m] = m
		S.append(S[m] + files[m])
	# i는 1에서 3까지 순회
	for i in range(1, n):
		# j는 0에서 (3까지, 2까지, 1까지)
		for j in range(n - i):
			# now = (1, 2, 3), (2, 3), (3)
			now = i + j  # 행 별로 now까지의 최소비용을 계산해줘야 한다.
			D[j][now] = sys.maxsize  # 우선 최대값으로 갱신해둔다.
			for k in range(D[j][now - 1], min(A[j + 1][now] + 1, now)): 
				minimum = D[j][now] + D[k + 1][now] + S[now + 1] - S[j]
				if D[j][now] > minimum:
					D[j][now] = minimum
					A[j][now] = k
	return	D[0][n - 1]


N = int(si())
answer = []

for i in range(N):
	files = list(map(int, si().split()))
	answer.append(dp(N, files))

for ans in answer:
	print(ans)