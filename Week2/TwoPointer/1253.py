# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
# 수의 위치가 다르면 값이 같아도 다른 수이다.

import sys

n = int(sys.stdin.readline())
arr = sorted(map(int, sys.stdin.readline().split()))

answer = 0


for i in range(n):
    start = 0
    end = n - 1
    while start < end:
        if start == i:
            start += 1
        elif end == i:
            end -= 1
        elif arr[start] + arr[end] == arr[i]:
            answer += 1
            break
        elif arr[start] + arr[end] > arr[i]:
            end -= 1
        else:
            start += 1

print(answer)
