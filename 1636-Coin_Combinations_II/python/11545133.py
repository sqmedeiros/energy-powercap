def solve():
    import sys
    input = sys.stdin.readline

    n,x=map(int,input().split())
    coins=list(map(int,input().split()))
    dp=[0 for _ in range(x+1) ] # d[s] so cach de tong la s
    dp[0]=1
    for coin in coins:
        for s in range(1,x+1):
            if s >=coin:
                dp[s]=(dp[s]+dp[s-coin])%(10**9+7)
    print(dp[x])
solve()