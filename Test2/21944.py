import sys
from collections import defaultdict
from heapq import heappop, heappush, merge

si = sys.stdin.readline


def miis(): return map(int, si().split())


def msis(): return map(str, si().split())


class Group:
    group_set = set()

    def __init__(self, prob: int):
        self.prob = prob
        self.min_heap = []
        self.max_heap = []

    @classmethod
    def del_set(cls, prob: int):
        cls.group_set.discard(prob)

    def solve(self, prob: int):
        sub_minheap = []
        sub_maxheap = []
        while self.min_heap and self.min_heap[0][1] != prob:
            heappush(sub_minheap, heappop(self.min_heap))
        if self.min_heap and self.min_heap[0][1] == prob:
            heappop(self.min_heap)
        while self.max_heap and -self.max_heap[0][1] != prob:
            heappush(sub_maxheap, heappop(self.max_heap))
        if self.max_heap and -self.max_heap[0][1] == prob:
            heappop(self.max_heap)
        self.min_heap = list(merge(sub_minheap, self.min_heap))
        self.max_heap = list(merge(sub_maxheap, self.max_heap))

    def self_heappop(self):
        while self.min_heap and (not not_solved.get(self.min_heap[0][1]) or self.min_heap[0][1] not in self.group_set):
            heappop(self.min_heap)
        while self.max_heap and (not not_solved.get(-self.max_heap[0][1]) or -self.max_heap[0][1] not in self.group_set):
            heappop(self.max_heap)

    def self_heappush(self, prob: int, difficulty: int):
        self.self_heappop()
        heappush(self.min_heap, (difficulty, prob))
        heappush(self.max_heap, (-difficulty, -prob))
        self.group_set.add(prob)

    def recommend1(self, X: int):
        self.self_heappop()
        if X == 1:
            if self.max_heap:
                return -self.max_heap[0][1]
            return False
        if self.min_heap:
            return self.min_heap[0][1]
        return False


class Difficulty:
    difficult_set = set()

    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.min_heap = []
        self.max_heap = []

    @classmethod
    def del_set(cls, prob: int):
        cls.difficult_set.discard(prob)

    def solve(self, prob: int):
        sub_maxheap = []
        sub_minheap = []
        while self.min_heap and self.min_heap[0] != prob:
            heappush(sub_minheap, heappop(self.min_heap))
        if self.min_heap and self.min_heap[0] == prob:
            heappop(self.min_heap)
        while self.max_heap and -self.max_heap[0] != prob:
            heappush(sub_maxheap, heappop(self.max_heap))
        if self.max_heap and -self.max_heap[0] == prob:
            heappop(self.max_heap)
        self.min_heap = list(merge(sub_minheap, self.min_heap))
        self.max_heap = list(merge(sub_maxheap, self.max_heap))

    def self_heappop(self):
        while self.max_heap and (not not_solved.get(-self.max_heap[0]) or -self.max_heap[0] not in self.difficult_set):
            heappop(self.max_heap)
        while self.min_heap and (not not_solved.get(self.min_heap[0]) or self.min_heap[0] not in self.difficult_set):
            heappop(self.min_heap)

    def self_heappush(self, prob: int):
        self.self_heappop()
        heappush(self.min_heap, prob)
        heappush(self.max_heap, -prob)
        self.difficult_set.add(prob)

    def recommend3(self, X: int):
        self.self_heappop()
        if X == -1:
            if self.max_heap:
                return -self.max_heap[0]
            return False
        if self.min_heap:
            return self.min_heap[0]
        return False


class Problem:
    max_heap = []
    min_heap = []

    def __init__(self, level, group):
        self.level = level
        self.group = group

    @classmethod
    def solve(cls, prob: int):
        sub_minheap = []
        sub_maxheap = []
        while cls.max_heap and -cls.max_heap[0][1] != prob:
            heappush(sub_maxheap, heappop(cls.max_heap))
        if cls.max_heap and -cls.max_heap[0][1] == prob:
            heappop(cls.max_heap)
        cls.max_heap = list(merge(cls.max_heap, sub_maxheap))
        while cls.min_heap and cls.min_heap[0][1] != prob:
            heappush(sub_minheap, heappop(cls.min_heap))
        if cls.min_heap and cls.min_heap[0][1] == prob:
            heappop(cls.min_heap)
        cls.min_heap = list(merge(cls.min_heap, sub_minheap))

    @classmethod
    def self_heappop(cls):
        while cls.max_heap and not not_solved.get(-cls.max_heap[0][1]):
            heappop(cls.max_heap)
        while cls.min_heap and not not_solved.get(cls.min_heap[0][1]):
            heappop(cls.min_heap)

    @classmethod
    def self_heappush(cls, prob: int, group: int, level: int):
        cls.self_heappop()
        heappush(cls.min_heap, (level, prob, group))
        heappush(cls.max_heap, (-level, -prob, group))

    @classmethod
    def recommend2(cls, X: int):
        cls.self_heappop()
        if X == 1:
            if cls.max_heap:
                return -cls.max_heap[0][1]
            return False
        if cls.min_heap:
            return cls.min_heap[0][1]
        return False


g_dict = defaultdict()
d_dict = defaultdict()
p_dict = defaultdict()
not_solved = defaultdict()
answer = []
n = int(si())
for _ in range(n):
    problem, level, group = miis()
    try:
        g_dict[group].self_heappush(prob=problem, difficulty=level)
    except KeyError:
        g_dict[group] = Group(prob=group)
        g_dict[group].self_heappush(prob=problem, difficulty=level)
    try:
        d_dict[level].self_heappush(prob=problem)
    except KeyError:
        d_dict[level] = Difficulty(difficulty=level)
        d_dict[level].self_heappush(prob=problem)
    try:
        p_dict[problem].self_heappush(level=level, group=group)
    except KeyError:
        p_dict[problem] = Problem(level=level, group=group)
        p_dict[problem].self_heappush(prob=problem, level=level, group=group)
    not_solved[problem] = True

m = int(si())
for _ in range(m):
    line = si().split()
    if line[0] == 'solved':
        p = int(line[1])
        del not_solved[p]
        lv, g = p_dict[p].level, p_dict[p].group
        d_dict[lv].del_set(prob=p)
        g_dict[g].del_set(prob=p)
        d_dict[lv].solve(prob=p)
        g_dict[g].solve(prob=p)
        del p_dict[p]

    elif line[0] == 'add':
        p, lv, g = map(int, line[1:])
        if p_dict.get(p):
            p_dict[p].solve(prob=p)
        try:
            d_dict[lv].self_heappush(prob=p)
        except KeyError:
            d_dict[lv] = Difficulty(difficulty=p)
            d_dict[lv].self_heappush(prob=p)
        try:
            g_dict[g].self_heappush(prob=p, difficulty=lv)
        except KeyError:
            g_dict[g] = Group(prob=p)
            g_dict[g].self_heappush(prob=p, difficulty=lv)
        try:
            p_dict[p].self_heappush(prob=p, level=lv, group=g)
        except KeyError:
            p_dict[p] = Problem(level=lv, group=g)
            p_dict[p].self_heappush(prob=p, group=g, level=lv)
        not_solved[p] = True

    else:
        ret = -1
        if line[0] == 'recommend':
            g, x = map(int, line[1:])
            ret = g_dict[g].recommend1(X=x)

        elif line[0] == 'recommend2':
            x = int(line[1])
            ret = Problem.recommend2(X=x)
        else:
            x, lv = map(int, line[1:])
            if x == -1:
                lv += x
            while 0 < lv <= 100:
                if d_dict.get(lv):
                    ret = d_dict[lv].recommend3(X=x)
                    if ret:
                        break
                lv += x
        if not ret:
            ret = -1
        answer.append(ret)

for ans in answer:
    print(ans)
