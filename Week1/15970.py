import sys

arr = []
answer = 0
N = int(sys.stdin.readline())
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x: x[0])
for j in range(N):
    temp = [abs(k[0] - arr[j][0]) for k in arr if k != arr[j] and k[1] == arr[j][1]]
    answer += min(temp)

print(answer)
