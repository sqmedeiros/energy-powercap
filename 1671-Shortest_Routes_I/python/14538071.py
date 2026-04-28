import heapq
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n+1)]
    index = 2
    for i in range(m):
        a = int(data[index]); b = int(data[index+1]); c = int(data[index+2]); index += 3
        graph[a].append((b, c))

    INF = 10**18
    dist = [INF] * (n+1)
    dist[1] = 0

    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        d, node = heapq.heappop(heap)
        if d != dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_d = d + weight
            if new_d < dist[neighbor]:
                dist[neighbor] = new_d
                heapq.heappush(heap, (new_d, neighbor))

    print(" ".join(str(dist[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()