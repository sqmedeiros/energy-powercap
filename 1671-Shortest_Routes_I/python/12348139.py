import heapq
import sys

def dijkstra(n, graph):
    INF = float('inf')
    dist = [INF] * (n + 1)   
    dist[1] = 0   
    pq = [(0, 1)]   

    while pq:
        d, u = heapq.heappop(pq)   
        if d > dist[u]:  
            continue
        for v, length in graph[u]:   
            new_dist = d + length
            if new_dist < dist[v]:   
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist[1:]  
def main():

    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))  


    result = dijkstra(n, graph)


    print(*result)

if __name__ == "__main__":
    main()