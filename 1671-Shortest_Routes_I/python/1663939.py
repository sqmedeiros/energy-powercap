import sys
from heapq import heappop, heappush


def dijkstra(n, graph, start):
    """ Uses Dijkstra's algortihm to find the shortest path between in a graph. """
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents


def main():

    #for _ in range(int(sys.stdin.readline().strip())):
    V,E=map(int,sys.stdin.readline().strip().split())
    graph={i:[] for i in range(V)}
    for i in range(E):
        x,y,w=map(int,input().split())
        x-=1
        y-=1
        graph[x].append((y,w))     

    dist,parents=dijkstra(V,graph,0)  
    print(*dist)


main()