from collections import Counter
import re

s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s3 = "{{20,111},{111}}"
s4 = "{{123}}"
s5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"


def solution(s):
    arr = s.replace('{', "")
    arr = arr.replace('}', "")
    arr = list(map(int, arr.split(',')))
    counter = Counter(arr)
    answer = list(counter.keys())
    answer.sort(reverse=True, key=lambda x: counter[x])
    return answer


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
