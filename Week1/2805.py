# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다.
# (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에,
# 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.


import sys

n, m = map(int, sys.stdin.readline().split())
trees = sorted(map(int, sys.stdin.readline().split()))

start = trees[-1]
end = 0

while start >= end:
    mid = (start + end) // 2
    height = sum([i - mid for i in trees if i > mid])
    if height >= m:
        end = mid + 1
    else:
        start = mid - 1
# 같다 조건만 다르게 했는데 하나는 틀렸습니다, 하나는 정답처리 됨
# mid 로 자르는데 목표 높이를 달성했다면 바로 끝내면 된다고 생각했는데, 어떤 예외가 있는지 모르겠다.
print(start)
