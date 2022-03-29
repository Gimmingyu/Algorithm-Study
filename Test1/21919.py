from math import sqrt
import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
prime_list = []


def is_prime(x):
    for num in range(2, int(sqrt(x)) + 1):
        if x % num == 0:
            return
    prime_list.append(x)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


for z in arr:
    is_prime(z)

answer = 1

if prime_list:
    for p in prime_list:
        answer = lcm(answer, p)
    print(answer)
else:
    print(-1)
