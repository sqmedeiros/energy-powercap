n = int(input())
a = list(map(int,input().split()))
ans = a[0]
cur = a[0]
for i in range(1,n):
    cur = max(a[i],cur+a[i])
    ans = max(ans,cur)
print(ans)