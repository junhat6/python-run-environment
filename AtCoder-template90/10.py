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
    ten1 = [0] * (N + 1)
    ten2 = [0] * (N + 1)

    for i in range(N):
        c, p = map(int, input().split())
        if c == 1:
            ten1[i + 1] = ten1[i] + p
            ten2[i + 1] = ten2[i]
        if c == 2:
            ten2[i + 1] = ten2[i] + p
            ten1[i + 1] = ten1[i]

    Q = int(input())
    for i in range(Q):
        f, l = map(int, input().split())
        ans1 = 0
        ans2 = 0
        ans1 = ten1[l] - ten1[f - 1]
        ans2 = ten2[l] - ten2[f - 1]
        print(ans1, ans2)


if __name__ == "__main__":
    solve()
