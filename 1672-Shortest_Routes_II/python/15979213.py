import sys
import heapq

# Constants
INF = 10**15

def solve_dijkstra_n_times(n, m, q, iterator):
    # --- Strategy: N x Dijkstra ---
    # Best for Sparse/Medium graphs (Tests 1-13)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist_matrix = [[INF] * (n + 1) for _ in range(n + 1)]

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
    # --- Strategy: Optimized Floyd-Warshall ---
    # Best for Dense graphs (Tests 14-16)
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

    # Optimization: Hoist row lookups
    nodes = range(1, n + 1)
    for k in nodes:
        dist_k = dist[k]
        for i in nodes:
            dist_ik = dist[i][k]
            if dist_ik == INF: continue # Pruning

            dist_i = dist[i]
            for j in nodes:
                # Manual Check allows PyPy to optimize better than min()
                if dist_ik + dist_k[j] < dist_i[j]:
                    dist_i[j] = dist_ik + dist_k[j]
    return dist

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)

    try:
        n = int(next(iterator))
        m = int(next(iterator))
        q = int(next(iterator))
    except StopIteration: return

    # --- THE CRITICAL FIX ---
    # Switch algorithms based on graph density
    # 100,000 is the approximate break-even point for Python
    if m >= 100000:
        dist_matrix = solve_floyd_warshall(n, m, q, iterator)
    else:
        dist_matrix = solve_dijkstra_n_times(n, m, q, iterator)

    # Output
    output = []
    for _ in range(q):
        u = int(next(iterator))
        v = int(next(iterator))
        ans = dist_matrix[u][v]
        output.append("-1" if ans == INF else str(ans))
    print('\n'.join(output))

if __name__ == '__main__':
    solve()