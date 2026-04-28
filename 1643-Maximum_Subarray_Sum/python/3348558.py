import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
LOGN = 20
INF = 10 ** 9 + 5
MOD = 10 ** 9 + 7
# ============================ START OF MY CODE ============================

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    ans = - INF
    res = 0
    for x in A:
        res = max(res + x, x)
        ans = max(ans, res)
    print(ans)

if __name__ == "__main__":
    solve()