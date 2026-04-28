import sys

input = sys.stdin.readline

def solve():

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 0

    for mask in range(1, 1 << k):
        cur = 1
        amt = 0

        for i in range(k):
            if mask & (1 << i):
                cur *= arr[i]
                amt ^= 1

        # dp[mask] = n // cur

        if amt:
            ans += n // cur

        else:
            ans -= n // cur

    print(ans)

solve()