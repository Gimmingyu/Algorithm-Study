from collections import Counter
import sys, time

arr = []
N = int(sys.stdin.readline())

for i in range(N):
    arr.append(int(sys.stdin.readline()))

start = time.time()
dic = Counter(arr)
print((max(dic.keys(), key=lambda x: (dic[x], -x))))
print(time.time() - start)
