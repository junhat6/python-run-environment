# main.py
import sys
import math

input = sys.stdin.readline  # 高速入力


def solve():
    h, w = map(int, input().split())
    a = (h + 1) // 2
    b = (w + 1) // 2
    ans = a * b
    print(ans)


if __name__ == "__main__":
    solve()

# set重複がない検索が高速
