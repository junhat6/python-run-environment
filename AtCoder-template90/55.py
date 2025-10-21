# main.py
import sys
import math
from itertools import combinations


input = sys.stdin.readline  # 高速入力


def solve():
    n, p, q = map(int, input().split())
    nums = []
    nums = list(map(int, input().split()))

    ans = 0
    combs = combinations(nums, 5)
    for a, b, c, d, e in combs:
        if ((a % p) * (b % p) * (c % p) * (d % p) * (e % p)) % p == q:
            ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
