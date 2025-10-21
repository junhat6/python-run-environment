# main.py
import sys
import math
from itertools import combinations
from collections import deque

input = sys.stdin.readline  # 高速入力


def solve():
    q = int(input())
    d = deque()
    ans = []
    for _ in range(q):
        a, b = map(int, input().split())
        if a == 1:
            d.appendleft(b)
        if a == 2:
            d.append(b)
        if a == 3:
            ans.append(str(d[b - 1]))
    print("\n".join(ans))


if __name__ == "__main__":
    solve()
