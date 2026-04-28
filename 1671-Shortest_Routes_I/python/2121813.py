import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from heapq import *
INF=99**9
n,m=map(int,input().split())
adj=[[] for _ in range(n)]
distances_=[]
for i in range(m):
    s,e,w=map(int,input().split())
    adj[s-1].append((e,w))
nn=0
pq=[]
heapify(pq)
processed=[0]*n
distances=[INF]*n
distances[nn]=0
heappush(pq,(0,nn+1))
while len(pq) != 0:
    searched_distance,searched=heappop(pq)
    if processed[searched-1]:
        continue
    else:
        processed[searched-1]=True
        for i in adj[searched-1]:
            e,w=i[0],i[1]
            if searched_distance+w<distances[e-1]:
                distances[e-1]=searched_distance+w
                heappush(pq,(distances[e-1],e))
distances_.append(distances)
for _ in range(n):
    s,e=1,_+1
    result=distances_[s-1][e-1]

    sys.stdout.write(str(result) + " ")
