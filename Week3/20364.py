from collections import deque
import sys

si = sys.stdin.readline

n, q = map(int, si().split())

wanted = [-1] * q
current = [False] * (n + 1)
for duck in range(q):
    wanted[duck] = int(si())


def solution(arr):
    # 목적지리스트 순회
    for dest in arr:
        # temp에 목적지 저장
        temp = dest
        # flag 설정 -->
        flag = True
        # temp가 0이 될 때 까지 2로 나누어준다. --> 경로를 알 수 있음
        while temp > 0:
            # 만약 2로 나눈 몫의 current가 참이면 이미 구매된 땅.
            if current[temp // 2]:
                # flag를 줘서 도착못했음을 알린다.
                flag = False
                # print 해준다.
                yield temp // 2
                break
            else:
                # 리프에서 현재까지는 구매된 땅이 없었으므로 계속 진행
                temp //= 2

        # 경로에는 구매된 땅이 없으나, 목적지가 구매된 경우
        if flag and current[dest]:
            yield dest
        # 경로에도 구매된 땅이 없었고ㅡ 목적지도 구매되지 않았다.
        elif flag:
            # true로 만들어주고 0 print
            current[dest] = True
            yield 0


for ans in solution(wanted):
    print(ans)
