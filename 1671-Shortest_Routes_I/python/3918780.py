import sys,os,io
import math
from collections import defaultdict
import heapq


# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

def output(a):
    if a is not list:
        sys.stdout.write(str(a) + "\n")
    else:
        sys.stdout.write(" ".join(map(str,a)) + "\n")



def linput():
    return list(minput())

def minput():
    return map(int, input().strip().split())

mod=10**9+7

#################################################################################

def main():    
    n,m=minput()
    adj=[[] for j in range(n)]
    for i in range(m):
        x,y,z=minput()
        x-=1
        y-=1
        adj[x].append([y,z])
    # print(adj)
    dist=[math.inf for i in range(n)]
    vis=[False for i in range(n)]
    dist[0]=0
    edges=[(0,0)]

    while len(edges)!=0:
        cur=heapq.heappop(edges)
        ind=cur[1]
        if vis[ind]:
            continue
        vis[ind]=True
        for neigbour in adj[ind]:
            node,wt=neigbour[0],neigbour[1]
            if dist[node] > dist[ind] + wt:
                dist[node]=dist[ind]+wt
                heapq.heappush(edges, (dist[node],node))

    for i in dist:
        print(i, end=' ')




#############################################################################

if __name__ == '__main__':
    main()