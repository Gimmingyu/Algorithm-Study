# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.


from collections import deque
import sys

# n을 입력 받는다
n = int(sys.stdin.readline())

# 문제에서 root는 1로 고정되어있음.
root = 1

# 각 노드의 부모를 저장해줄 리스트
parent = [0] * n

# n-1줄 입력을 받아서 큐에 넣는다.
q = deque()
for _ in range(n - 1):
    # 깔끔하게 볼 수 있도록 sorted 사용해서 숫자가 작은 노드가 앞에 오도록 했다.
    q.append(sorted(map(int, sys.stdin.readline().split())))


# 부모를 찾을 때, 아직 정보가 없어서 누가 부모인지 모를 수 있다.
# flag를 줘서 부모찾기의 성공여부를 return 한다.
def find_parent_node(first, second):
    global parent
    if parent[first]:
        parent[second] = first
        return True
    elif parent[second]:
        parent[first] = second
        return True
    else:
        return False


# 저장한 큐를 순회하면서
while q:
    # 연결된 두 노드를 x와 y로 지정한다.
    x, y = q.popleft()
    print(f"x = {x}, y = {y}")
    # (x)가 항상 작으므로, 만약 x가 루트라면 루트 바로 밑(깊이1)이므로 저장해주고 continue
    # root와 연결된 노드들부터 부모가 찾아진다.
    if x == root:
        parent[y] = root
        print(f"parent = {parent}")
        continue
    # 루트가 아니라면, 둘 중 누가 부모인지 찾아줘야 한다.
    else:
        flag = find_parent_node(x, y)
        if not flag:
            q.append([x, y])
    print(f"parent = {parent}")

print(i for i in parent)