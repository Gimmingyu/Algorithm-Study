from collections import deque


def solution(stones, k):
    answer = 0
    start = 1
    end = 200000000

    while start <= end:
        mid = (start + end) // 2
        temp = k
        for now in stones:
            if now - mid < 0:
                temp -= 1
            else:
                temp = k
            if not temp:
                end = mid - 1
                break

        if temp:
            answer = mid
            start = mid + 1

    return answer


stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3
print(solution(stones, k))
