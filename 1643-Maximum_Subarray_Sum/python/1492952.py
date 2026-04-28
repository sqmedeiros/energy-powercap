n=int(input())
ls=[int(x) for x in input().split(' ')]
m=0
ans=ls[0]
for i in range (n):
    m=max(ls[i],m+ls[i])
    ans = max(ans,m)
print(ans)