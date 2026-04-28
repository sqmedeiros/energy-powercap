n=int(input())
a=list(map(int,input().split()))
dp=[-float('inf')]*(n+1)
if n==1:
    print(a[0])
else:
    dp[0]=a[0]
    dp[1]=max(a[1]+a[0],a[1])
    for i in range(2,n):
        dp[i]=max(a[i],dp[i-1]+a[i])
    print(max(dp))