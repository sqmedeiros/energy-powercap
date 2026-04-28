import sys
import heapq

def main():
    read = sys.stdin.readline
    nodes, edges = map(int, read().split())

    adj = [[] for _ in range(nodes + 1)]

    for _ in range(edges):
        x, y, wt = map(int, read().split())
        adj[x].append((y, wt))

    INF = 10**18
    dist = [INF] * (nodes + 1)
    dist[1] = 0

    pq = [(0, 1)]

    while pq:
        cur_w, cur = heapq.heappop(pq)

        if cur_w != dist[cur]:
            continue

        for nxt, cost in adj[cur]:
            new_w = cur_w + cost
            if new_w < dist[nxt]:
                dist[nxt] = new_w
                heapq.heappush(pq, (new_w, nxt))

    print(" ".join(str(dist[i]) for i in range(1, nodes + 1)))

if __name__ == "__main__":
    main()