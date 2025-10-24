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
    h, w = map(int, input().split())
    A = []
    for _ in range(h):
        row = list(map(int, input().split()))
        A.append(row)

    yoko = list(map(sum, A))
    tate = list(map(sum, zip(*A)))

    B = []

    for i in range(h):
        line = []
        for j in range(w):
            value = yoko[i] + tate[j] - A[i][j]
            line.append(str(value))
        print(" ".join(line))


if __name__ == "__main__":
    solve()
