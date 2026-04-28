import sys
import heapq

# Set recursion limit higher for potentially deep operations, and faster input reading
# We read all input once and process it.
sys.setrecursionlimit(2000)

def solve():
    # Read all input lines
    try:
        input_data = sys.stdin.read().split()
    except:
        return

    if not input_data:
        return

    data_iter = iter(input_data)

    try:
        N = int(next(data_iter)) # Number of cities
        M = int(next(data_iter)) # Number of flights
    except StopIteration:
        return

    # 1. Build the Adjacency List
    # adj[u] = list of (v, w) pairs, meaning flight u -> v with length w
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        try:
            a = int(next(data_iter))
            b = int(next(data_iter))
            c = int(next(data_iter))
            adj[a].append((b, c))
        except StopIteration:
            break

    # 2. Initialization
    # Use a large number for infinity. 10^9 * 10^5 = 10^14 is the max possible distance.
    INF = float('inf') 
    dist = [INF] * (N + 1)

    # Syrjälä (City 1) is the source
    start_node = 1
    dist[start_node] = 0

    # Priority Queue (min-heap): stores tuples of (distance, city)
    pq = [(0, start_node)]

    # 3. Processing (Dijkstra's Algorithm)
    while pq:
        # Get the city 'u' with the minimum known distance 'd'
        d, u = heapq.heappop(pq)

        # Skip stale entries
        if d > dist[u]:
            continue

        # Relax neighbors
        for v, weight in adj[u]:
            new_dist = d + weight

            # If a shorter path to 'v' is found
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    # 4. Output: Print the shortest route lengths to cities 1 to N
    results = []
    for i in range(1, N + 1):
        # The problem requires printing the shortest route length. 
        # If the distance is still INF, it means the city is unreachable, 
        # but the constraint says it is possible to travel to all cities.
        # We check for INF just in case of slight errors or unexpected input.
        if dist[i] == INF:
             # This branch should not be reached based on problem constraints
             results.append("-1") 
        else:
             results.append(str(dist[i]))

    sys.stdout.write(" ".join(results) + "\n")

if __name__ == "__main__":
    solve()