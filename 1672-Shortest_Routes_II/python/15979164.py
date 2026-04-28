import sys
import heapq

# Constants
INF = 10**15

def solve_n_dijkstra(n, m, q, iterator):
    # Dijkstra is faster for Sparse graphs
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w)) 

    # Dist matrix stores the shortest path from u to v
    dist_matrix = [[INF] * (n + 1) for _ in range(n + 1)]

    # Run Dijkstra for every node
    for start_node in range(1, n + 1):
        dist_matrix[start_node][start_node] = 0
        pq = [(0, start_node)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist_matrix[start_node][u]:
                continue

            for v, weight in adj[u]:
                if dist_matrix[start_node][u] + weight < dist_matrix[start_node][v]:
                    dist_matrix[start_node][v] = dist_matrix[start_node][u] + weight
                    heapq.heappush(pq, (dist_matrix[start_node][v], v))

    return dist_matrix

def solve_floyd_warshall(n, m, q, iterator):
    # Floyd-Warshall is faster for Dense graphs
    # 1. Build Adjacency Matrix
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # 2. Run O(N^3) Algorithm with optimizations
    # Pre-fetch range to avoid function call overhead
    rng = range(1, n + 1)

    for k in rng:
        # Optimization: Lift row_k lookup out of inner loops
        row_k = dist[k]

        for i in rng:
            # Optimization: Lift row_i lookup
            row_i = dist[i]

            # Optimization: Pruning
            dik = row_i[k]
            if dik == INF: 
                continue

            for j in rng:
                # Direct access is faster than dist[i][j]
                if dik + row_k[j] < row_i[j]:
                    row_i[j] = dik + row_k[j]

    return dist

def solve():
    # Read entire input at once
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)

    try:
        n = int(next(iterator))
        m = int(next(iterator))
        q = int(next(iterator))
    except StopIteration: return

    # --- HYBRID THRESHOLD ---
    # Tests show Dijkstra passes M=79k in 0.8s, but fails M=250k.
    # FW (Optimized) passes M=250k in 0.7s.
    # We set the switch point at 100,000 edges.
    if m >= 100000:
        dist_matrix = solve_floyd_warshall(n, m, q, iterator)
    else:
        dist_matrix = solve_n_dijkstra(n, m, q, iterator)

    # --- Output ---
    output = []
    for _ in range(q):
        u = int(next(iterator))
        v = int(next(iterator))
        ans = dist_matrix[u][v]
        output.append("-1" if ans == INF else str(ans))

    print("\n".join(output))

if __name__ == "__main__":
    solve()