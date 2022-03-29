from heapq import *
from collections import defaultdict
import sys

si = sys.stdin.readline
n, m = map(int, si().split())
total = 0
graph = []
for _ in range(m):
    n1, n2, weight = map(int, si().split())
    graph.append((weight, n1, n2))
    total += weight


def prim(g, start):
    mst = 0
    # 모든 간선의 정보를 담을 트리
    tree = defaultdict(list)
    for w, b1, b2 in g:
        tree[b1].append((w, b1, b2))
        tree[b2].append((w, b2, b1))
    # 방문할 노드가 담긴 세트
    visited = set()
    visited.add(start)
    # 시작노드와 연결된 간선들의 리스트
    candidate_arr = tree[start]
    # 시작 노드와 연결된 간선들을 힙 자료구조로 만든다. --> 가중치가 작은 순서로 나온다.
    heapify(candidate_arr)
    # print(f"candidate arr = {candidate_arr}")
    while candidate_arr:
        # 가중치, 현재 노드와 연결된 노드가 나옴.
        w, b1, b2 = heappop(candidate_arr)
        # print(f"heappop! w = {w}, b1 = {b1}, b2 = {b2}")
        # 만약 연결된 노드가 방문하지 않았다면
        if b2 not in visited:
            # 방문처리를 한다. --> 현재 노드와 연결된 간선중 가장 가중치가 작으면서 가본 적이 없는 노드
            visited.add(b2)
            # 가중치를 더해준다.
            mst += w
            # print(f"visited = {visited}, now answer is {mst}")
            # 다음 방문할 노드와 연결된 노드들을 순회
            for node in tree[b2]:
                # 방문한 적이 없는 노드라면 힙에 넣는다.
                if node[2] not in visited:
                    # print(f"add candidate {node[2]}")
                    heappush(candidate_arr, node)
                    # print(f"now candidate_arr = {candidate_arr}")
    # print(f"total = {total}")
    # print(f"mst = {mst}")
    return visited, total - mst


check, answer = prim(graph, 1)
if len(check) == n:
    print(answer)
else:
    print(-1)
