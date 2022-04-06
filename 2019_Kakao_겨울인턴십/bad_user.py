
user_id1, banned_id1 = ["frodo", "fradi", "crodo",
                        "abc123", "frodoc"], ["fr*d*", "abc1**"]
user_id2, banned_id2 = ["frodo", "fradi", "crodo",
                        "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
user_id3, banned_id3 = ["frodo", "fradi", "crodo",
                        "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]


def solution(user_id, banned_id):

    idx = [[i for i in range(len(id)) if id[i] == '*']
           for id in banned_id]

    table = [[] for _ in range(len(banned_id))]
    for uid in user_id:
        for bid in range(len(banned_id)):
            if len(uid) == len(banned_id[bid]):
                compare = bytearray(uid, encoding='utf8')
                for i in range(len(idx[bid])):
                    compare[idx[bid][i]] = ord('*')
                if compare.decode() == banned_id[bid]:
                    table[bid].append(uid)

    answer = 0
    s_list = []
    for i in table[0]:
        s = set()
        s.add(i)
        if not table[0]:
            return 0
        for j in range(1, len(table)):
            if not table[j]:
                return 0
            for k in range(len(table[j])):
                if table[j][k] in s:
                    continue
                else:
                    s.add(table[j][k])
                    break
        if s not in s_list:
            s_list.append(s)
    return s_list


print(solution(user_id1, banned_id1))
print(solution(user_id2, banned_id2))
print(solution(user_id3, banned_id3))
