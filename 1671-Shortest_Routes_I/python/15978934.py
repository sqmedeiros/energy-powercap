import sys
import heapq

# 1. Essential for Recursive DFS on large graphs (N=100,000)
sys.setrecursionlimit(200005)

def solve():
    # --- Input Parsing ---
    # Read all at once for speed
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)

    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration: return

    # Build Graph (1-indexed)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        # adj[v].append((u, w))

    def dijkstra(start_node, adj, n, m):
        dist = [float("inf")] * (n + 1)
        dist[start_node] = 0
        min_heap = [(0, start_node)]

        while min_heap:
            time, curr_city = heapq.heappop(min_heap)

            if time > dist[curr_city]:
                continue

            for nei, w in adj[curr_city]:
                if time + w < dist[nei]:
                    dist[nei] = time + w
                    heapq.heappush(min_heap, (time + w, nei))

        return dist

    dist = dijkstra(1, adj, n, m)

    print(*dist[1:])




if __name__ == "__main__":
    solve()