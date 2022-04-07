user_id1, banned_id1 = ["frodo", "fradi", "crodo",
                        "abc123", "frodoc"], ["fr*d*", "abc1**"]
user_id2, banned_id2 = ["frodo", "fradi", "crodo",
                        "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
user_id3, banned_id3 = ["frodo", "fradi", "crodo",
                        "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]

from itertools import product

def solution(user_id, banned_id):
    def permutations(array, r):
        for i in range(len(array)):
            if r == 1:
                yield [array[i]]
            else:
                for NEXT in permutations(array[:i] + array[i + 1:], r - 1):
                    yield [array[i]] + NEXT

    idx = [[i for i in range(len(d)) if d[i] == '*']
           for d in banned_id]

    table = [[] for _ in range(len(banned_id))]
    for uid in user_id:
        for bid in range(len(banned_id)):
            if len(uid) == len(banned_id[bid]):
                compare = bytearray(uid, encoding='utf8')
                for i in range(len(idx[bid])):
                    compare[idx[bid][i]] = ord('*')
                if compare.decode() == banned_id[bid]:
                    table[bid].append(uid)

    a = list(product(*table))
    s_list = []
    for i in a:
        b = set(i)
        if b not in s_list and len(b) == len(table):
            s_list.append(b)
    return s_list


print(solution(user_id1, banned_id1))
print(solution(user_id2, banned_id2))
print(solution(user_id3, banned_id3))
