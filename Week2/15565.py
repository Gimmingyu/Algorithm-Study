import sys

n, k = map(int, sys.stdin.readline().split())

dolls = sys.stdin.readline().split()

start, end, count = 0, 0, 0
answer = sys.maxsize

while True:
    # start와 end 모두 양방향으로 증가.
    if count >= k:  # count가 k보다 크다면 start를 증가시킨다.
        answer = min(answer, end - start)
        if dolls[start] == '1':  # 이 때, start번째 인형이 라이언이면 count는 하나 줄인다.
            count -= 1
        start += 1
    elif end == n:  # end가 끝까지 이동했다면 종료
        break
    else:  # count가 k보다 작다면 end를 이동시킨다.
        if dolls[end] == '1':  # 이 때, 현재 담은 인형이 라이언이면 count를 증가시킨다.
            count += 1
        end += 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
