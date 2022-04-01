import sys

si = sys.stdin.readline
def MIIS(): return map(int, si().split())


n = int(si())

prob = {k: [] for k in range(101)}
idx = {}
for _ in range(n):
    num, difficulty = MIIS()
    prob[difficulty].append(num)
    idx[num] = difficulty

_max = max(x for x in prob if prob[x])
_min = min(x for x in prob if prob[x])
m = int(si())
ret = []

for _ in range(m):
    line = si().split()
    if line[0] == 'add':
        num, diff = map(int, line[1:])
        if diff < _min:
            _min = diff
        elif diff > _max:
            _max = diff
        prob[diff].append(num)
        idx[num] = diff
    elif line[0] == 'solved':
        num = int(line[1])
        if num in prob[_min]:
            prob[idx[num]].remove(num)
            _min = min(x for x in prob if prob[x])
        elif num in prob[_max]:
            prob[idx[num]].remove(num)
            _max = max(x for x in prob if prob[x])
        else:
            prob[idx[num]].remove(num)
    elif line[0] == 'recommend':
        if line[1] == '-1':
            ret.append(sorted(prob[_min])[0])
        else:
            ret.append(sorted(prob[_max])[-1])

for a in ret:
    print(a)
