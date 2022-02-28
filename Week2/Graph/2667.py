from collections import deque, Counter
import sys

n = int(sys.stdin.readline())
linked_node = {k: [] for k in range(n ** 2)}

for v in linked_node:
    if v % n != n - 1:
        linked_node[v].append(v + 1)
    if v >= n:
        linked_node[v].append(v - n)
    if v % n != 0:
        linked_node[v].append(v - 1)
    if v < n * (n - 1):
        linked_node[v].append(v + n)

table = ['0'] * (n ** 2)
case = -1


def solution(idx, c):
    global table
    table[idx] = c
    for node in linked_node[idx]:
        if table[node] == '1':
            solution(node, c)


for i in range(n):
    temp = sys.stdin.readline()
    for j in range(n):
        if temp[j] != '\n':
            table[i * n + j] = temp[j]

for k in range(len(table)):
    if table[k] == '1':
        solution(k, case)
        case -= 1
counter = Counter(table)
if '0' in counter:
    counter.pop('0')
answer = sorted(counter.values())

print(len(answer))
if answer:
    for i in answer:
        print(i)
