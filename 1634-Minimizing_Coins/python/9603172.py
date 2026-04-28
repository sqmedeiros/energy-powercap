def minimizing_coins(n,x,coins):
    dp=[float("INF")]*(x+1)
    dp[0]=0
    for i in range(x):
        if dp[i]==float("INF"):
            continue
        for j in coins:
            if i+j>x:
                continue
            dp[i+j]=min(dp[i+j],dp[i]+1)
    print(dp[x]) if dp[x]!=float("INF") else print(-1)
n,x=map(int,input().split(" "))
minimizing_coins(n,x,[*map(int,input().split(" "))])