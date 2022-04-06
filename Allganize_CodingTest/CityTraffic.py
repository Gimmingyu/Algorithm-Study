import sys, json
from collections import defaultdict, deque

given = ["1:[5]", "2:[5]", "3:[5]", "4:[5]", "5:[1,2,3,4]"]
given2 = ["1:[5]", "2:[5, 18]", "3:[5]", "4:[5]", "5:[1,2,3,4]"]


def city_traffic(string, n):
    link = defaultdict(list)
    table = defaultdict()
    visited = defaultdict()
    q = deque()
    for _ in string:
        idx, elem = int(_[0]), list(map(int, _[3:-1].split(',')))
        link[idx] = elem
        table[idx] = idx
        for j in elem:
            table[j] = j
        q.append((idx, idx))
    while q:
        _from, now = q.popleft()
        if not link[now]:
            continue
        for _next in link[now]:  # 5 /
            q.append((_from, _next))
            table[_from] += table[_next]
    print(table)

print(city_traffic(given, len(given)))
print(city_traffic(given2, len(given2)))
