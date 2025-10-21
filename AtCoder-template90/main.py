# main.py
import sys
import math

input = sys.stdin.readline  # 高速入力


def solve():
    h, w = map(int, input().split())
    if h == 1 or w == 1:
        print(h * w)
    else:
        a = (h + 1) // 2
        b = (w + 1) // 2
        print(a * b)


if __name__ == "__main__":
    solve()
