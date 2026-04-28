from collections import defaultdict
def f(l,k):
  g=defaultdict(list)
  for i in range(len(l)):
    for j in range(i):
      g[l[i]+l[j]].append((i,j))
  for val in g:
    req=k-val
    res=g.get(req,[])
    for pair1 in g[val]:
      for pair2 in res:
        temp=[pair1[0],pair1[1],pair2[0],pair2[1]]
        if len(set(temp))==4:
          return [pair1[0]+1,pair1[1]+1,pair2[0]+1,pair2[1]+1]
  return ["IMPOSSIBLE"]

n,k=map(int,input().strip().split())
l=list(map(int,input().strip().split()))
print(*f(l,k))