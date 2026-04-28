n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
v=[0]*2+[-1]*(n-1)
q=[]
q.append(1)
while q:
    qe=q.pop(0)
    for i in adj[qe]:
        if v[i]==-1: v[i]=qe; q.append(i)
if(v[n]==-1): print("IMPOSSIBLE")
else:
    ans=[]
    i=n
    while i!=0:
        ans.append(i)
        i=v[i]
    ans.reverse()
    print(len(ans))
    print(" ".join(map(str,ans)))