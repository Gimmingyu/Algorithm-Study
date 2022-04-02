import sys
from collections import defaultdict
from datetime import datetime, timedelta


def si(): return sys.stdin.readline()


def msis(): return map(str, si().split())


n, l, f = msis()
n, f, maximum = int(n), int(f), timedelta(days=int(l[:3]), hours=int(l[4:6]), minutes=int(l[7:]))
minute = timedelta(minutes=1)
table = defaultdict(dict)
p_table = defaultdict()
for _ in range(n):
    line = si()
    now = datetime.strptime(line[:16], '%Y-%m-%d %H:%M')
    part, name = line[16:].split()
    if not p_table.get(name):
        p_table[name] = 0
    if table[name].get(part):
        period = now - table[name][part]
        if period > maximum:
            p_table[name] += ((period - maximum) // minute) * f
        del table[name][part]
    else:
        table[name][part] = now

ret = [(k, v) for k, v in p_table.items() if v]
if ret:
    for name, val in sorted(ret, key=lambda x: x[0]):
        print(name, val)
else:
    print(-1)

