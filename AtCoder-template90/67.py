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
    n, k = map(int, input().split())

    def base10_to_base9(num: int) -> str:
        if num == 0:
            return "0"
        s = []
        while num > 0:
            amari = num % 9
            s.append(str(amari))
            num = num // 9
        return "".join(reversed(s))

    n_str = str(n)
    for _ in range(k):
        val = int(n_str, 8)
        s9 = base10_to_base9(val)
        s9 = s9.replace("8", "5")
        n_str = s9
    print(n_str)


if __name__ == "__main__":
    solve()
