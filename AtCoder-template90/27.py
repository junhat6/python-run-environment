# main.py
import sys
import math

input = sys.stdin.readline  # 高速入力


def solve():
    n = int(input())
    set_ = set()
    for i in range(1, n + 1):
        a = input()
        if a not in set_:
            set_.add(a)
            print(i)


if __name__ == "__main__":
    solve()

# set重複がない検索が高速
