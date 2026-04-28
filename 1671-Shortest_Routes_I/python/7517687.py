from sys import stdin
from sys import stdout
import queue
infinito = 200000000000000

def dijkstra(source): 
    q = queue.PriorityQueue() 

    dist[source] = 0
    q.put((0,source))

    while q.empty() == False:
        top = q.get()
        vertice = top[1] 
        peso = top[0] 
        if dist[vertice] >= peso:

            for proximo,aresta in ladj[vertice]: 
                if dist[proximo] > peso + aresta:
                    dist[proximo] = peso + aresta
                    q.put((dist[proximo],proximo))

n, m = map(int,stdin.readline().split())
ladj = [[] for j in range(n+1)]
dist = [infinito for j in range(n+1)]
for i in range(m):
 a,b,c = map(int, stdin.readline().split())
 ladj[a].append((b,c))

dijkstra(1)
for i in range(1,n+1):
 stdout.write(str(dist[i]) + " ")
