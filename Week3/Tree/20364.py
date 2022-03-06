import sys

si = sys.stdin.readline

n, q = map(int, si().split())

wanted = [int(si()) for _ in range(q)]
current = [False] * (n + 1)


def solution(arr):
    # 목적지리스트 순회
    for dest in arr:
        temp = dest
        if current[dest]:  # 만약 목적지가 이미 구매된 땅이라면 result에 저장
            result = dest
        else:  # 아니라면 우선 0을 저장한다.
            result = 0
        while dest > 1:  # dest가 1이 될 때 까지 2로 나누어준다. --> 경로를 알 수 있음
            if current[dest // 2]:  # 만약 2로 나눈 몫의 current가 참이면 이미 구매된 땅.
                result = dest // 2  # result를 갱신시켜준다. --> 경로 중 가장 1에 가까운 곳으로 계속 갱신
            dest //= 2
        current[temp] = True  # temp는 목적지가 구매되든 아니든 true (구매 못했으면 어차피 못가는 곳)
        yield result


for ans in solution(wanted):
    print(ans)
