a,b=map(int,input().split())
from collections import defaultdict
dic=defaultdict(list)
for _ in range(b):
    x,y=map(int,input().split())
    dic[x].append(y)
    dic[y].append(x)
def BFS(root):
    lis=[root]
    while len(lis):
        new=[]
        for j in lis:
            visited[j]=True
            for k in dic[j]:
                if not visited[k]:
                    new.append(k)
                    visited[k]=True
                    pred[k]=j
        lis=new
visited=[False for i in range(a+1)]
pred=[0 for i in range(a+1)]
BFS(1)
#print(pred)
ans=[]
if pred[a]==0:
    print("IMPOSSIBLE")
else:
    ans=[]
    while pred[a]!=1:
        ans.append(a)
        a=pred[a]
    ans.append(a)
    ans.append(1)
    print(len(ans))
    for j in ans[::-1]:
        print(j,end=" ")