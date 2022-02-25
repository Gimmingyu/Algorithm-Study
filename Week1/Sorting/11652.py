# # 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데,
# # 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오.
# # 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
#
from collections import Counter
import sys

arr = []
N = int(sys.stdin.readline())

for i in range(N):
    arr.append(int(sys.stdin.readline()))

dic = Counter(arr)
print((max(dic.keys(), key=lambda x: (dic[x], -x))))
