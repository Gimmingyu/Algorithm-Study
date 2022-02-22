# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다.
# 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000)

import sys

test_case = int(sys.stdin.readline())
answer = []
for test in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    lst_a = sorted(map(int, sys.stdin.readline().split()))
    lst_b = sorted(map(int, sys.stdin.readline().split()))
    # print(lst_a, lst_b)

    count = 0
    for i in lst_a:
        start = 0
        end = len(lst_b) - 1
        while start <= end:
            mid = (start + end) // 2
            if i > lst_b[mid]:
                start = mid + 1
            else:
                end = mid - 1
        count += end + 1
    answer.append(count)

for k in answer:
    print(k)
