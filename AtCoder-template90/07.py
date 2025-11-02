# main.py
import sys
import os
import math
from itertools import combinations
from collections import deque

# デバッグ時にinput.txtから読み込む
if os.getenv("INPUT_FILE"):
    sys.stdin = open(os.getenv("INPUT_FILE"), "r")

input = sys.stdin.readline  # 高速入力

from itertools import product
from bisect import bisect_left


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    INF = 10**18
    A = [-INF] + A + [INF]  # ← 番兵
    Q = int(input())
    out = []
    for _ in range(Q):
        b = int(input())
        j = bisect_left(A, b)
        out.append(str(min(b - A[j - 1], A[j] - b)))
    print("\n".join(out))


if __name__ == "__main__":
    solve()
