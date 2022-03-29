import sys

si = sys.stdin.readline
n, m = map(int, si().split())

arr = [0] + list(map(int, si().split()))


def command_1(i, x):
    global arr
    arr[i] = x


def command_2(l, r):
    global arr
    for idx in range(l, r + 1):
        if arr[idx] == 0:
            arr[idx] = 1
        else:
            arr[idx] = 0


def command_3(l, r):
    global arr
    for idx in range(l, r + 1):
        arr[idx] = 0


def command_4(l, r):
    global arr
    for idx in range(l, r + 1):
        arr[idx] = 1


def command(a, idx, x):
    global arr
    if a == 1:
        command_1(idx, x)
    elif a == 2:
        command_2(idx, x)
    elif a == 3:
        command_3(idx, x)
    elif a == 4:
        command_4(idx, x)


for i in range(m):
    a, b, c = map(int, si().split())
    command(a, b, c)

print(arr[1:])
