import sys

si = sys.stdin.readline
given = [6, 7, 3, 1, 100, 102, 6, 12]
given2 = [5, 6, 1, 2, 8, 9, 7]


def longest_consequtive(arr):
    counter = set(arr)
    _max = -sys.maxsize
    for i in counter:
        temp = 1
        now = i
        while True:
            if now + 1 not in counter:
                break
            now += 1
            temp += 1
        _max = max(_max, temp)
    return _max


print(longest_consequtive(given))
print(longest_consequtive(given2))
