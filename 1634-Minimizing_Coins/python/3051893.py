n,x = list(map(int,input().split()))
a = list(map(int,input().split()))
ans = [ 10**7 for _ in range(x+1)]
ans[0]=0
for i in a:
    for j in range(i,x+1):
        ans[j]=min(ans[j],ans[j-i]+1)
print((ans[x] if ans[x] != 10**7 else -1))