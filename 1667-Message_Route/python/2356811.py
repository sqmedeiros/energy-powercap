from math import *
from sys import stdin,setrecursionlimit
input=stdin.readline
# map(int,input().split())
setrecursionlimit(1000000)
def add_edge(adj, src, dest):
    adj[src].append(dest)
    adj[dest].append(src)

def BFS(adj, src, dest, v, pred, dist):
    queue = []
    visited = [False for i in range(v)]
    for i in range(v):
        dist[i] = 1000000
        pred[i] = -1
    visited[src] = True
    dist[src] = 0
    queue.append(src)
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):

            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
                if (adj[u][i] == dest):
                    return True
    return False

def printShortestDistance(adj, s, dest, v):
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)]
    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("IMPOSSIBLE")
    path = []
    crawl = dest
    crawl = dest
    path.append(crawl) 
    while (pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl]
    print(str(dist[dest]+1))
    for i in range(len(path)-1, -1, -1):
        print(path[i]+1,end=' ')

n,m=map(int,input().split())
adj = [[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    add_edge(adj,a-1,b-1)
printShortestDistance(adj,0,n-1,n)