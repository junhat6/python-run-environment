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


def solve():
    n, m = map(int, input().split())
    rinsetu = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        if a > b:
            rinsetu[a] += 1
        if b > a:
            rinsetu[b] += 1

    ans = 0
    for i in range(n + 1):
        if rinsetu[i] == 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
