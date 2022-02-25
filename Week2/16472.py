from collections import Counter
import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip('\n')

start, end = 0, 0
answer = 1
check = Counter()
for i in range(len(arr)):
    if not check[arr[i]]:
        check[arr[i]] = 1
    else:
        check[arr[i]] += 1
    while len(check) > n:
        if check[arr[start]] == 1:
            check.pop(arr[start])
        else:
            check[arr[start]] -= 1
        start += 1
    answer = max(answer, i - start + 1)

print(answer)



