# 점들의 위치와 색깔이 주어질 때, 모든 점에서 시작하는 화살표들의 길이 합을 출력하는 프로그램을 작성하시오.

import sys

arr = []
answer = 0
N = int(sys.stdin.readline())
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x: x[0])
for j in range(N):
    temp = [abs(k[0] - arr[j][0]) for k in arr if k != arr[j] and k[1] == arr[j][1]]
    # for k in arr:
    #     if k != arr[j] and k[1] == arr[j][1]:
    #         temp.append(abs(k[0] - arr[j][0]))
    answer += min(temp)

print(answer)
