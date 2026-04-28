if __name__=="__main__":
    n,x = map(int,input().split())
    c = list(map(int,input().split()))
    if x%c[-1]==0:
        print(x//c[-1])
    else:
        dp = [1000001]*(x+1)
        dp[0] = 0
        for i in range(1,x+1):
            for j in range(n):
                if i>=c[j] and dp[i-c[j]]<dp[i]-1:
                    dp[i] = dp[i-c[j]]+1
        if dp[x]>1000000:
            print(-1)
        else:
            print(dp[x])