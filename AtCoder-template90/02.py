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


def isValid(S: str):
    score = 0
    for c in S:
        if c == "(":
            score += 1
        else:
            score -= 1
        if score < 0:
            return False
    if score == 0:
        return True


def solve():
    n = int(input())

    if n % 2 == 1:
        return

    for S in product(["(", ")"], repeat=n):
        if isValid(S):
            print("".join(S))


if __name__ == "__main__":
    solve()
