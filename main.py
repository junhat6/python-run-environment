# main.py
import sys
input = sys.stdin.readline  # 高速入力

def solve():
    # 例:
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))

if __name__ == "__main__":
    solve()
