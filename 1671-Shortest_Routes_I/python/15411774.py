import sys
import heapq

# Set recursion limit higher for safety, although not strictly needed for iterative Dijkstra
# sys.setrecursionlimit(2000)
#code

def solve():
    # Read all input data for faster processing
    try:
        data = sys.stdin.read().split()
    except Exception:
        return

    if not data:
        return

    # Extract N (number of cities) and M (number of flights)
    N = int(data[0])
    M = int(data[1])

    # --- Step 1: Graph Representation (Adjacency List) ---
    # adj[u] will store a list of (v, weight) tuples
    adj = [[] for _ in range(N + 1)]

    # Process M flight connections
    data_index = 2
    for _ in range(M):
        a = int(data[data_index])
        b = int(data[data_index + 1])
        c = int(data[data_index + 2])

        # Add a directed edge from a to b with weight c
        adj[a].append((b, c))

        data_index += 3

    # --- Step 2: Initialization ---

    # A large value to represent infinity (max possible weight is 10^9)
    # 10^18 is safe for summation of up to 10^5 edges
    INF = 10**18 

    # distance[i] will store the shortest route length from city 1 to city i
    # We use size N+1 to keep 1-based indexing for cities 1..N
    distance = [INF] * (N + 1)

    # The starting city is 1 (Syrjälä)
    distance[1] = 0

    # Min-priority queue: stores (distance, city)
    # We start with the source city (distance 0)
    pq = [(0, 1)] # (distance_to_city, city_id)

    # --- Step 3: Exploration (Dijkstra's Algorithm) ---

    while pq:
        # Extract the node with the smallest distance
        d, u = heapq.heappop(pq)

        # Optimization: If we found a shorter path to u previously, skip this older entry
        if d > distance[u]:
            continue

        # Iterate over all flights (u -> v)
        for v, weight in adj[u]:
            new_dist = d + weight

            # If a shorter path to v is found through u
            if new_dist < distance[v]:
                distance[v] = new_dist
                # Add the new, shorter path to the priority queue
                heapq.heappush(pq, (new_dist, v))

    # --- Step 4: Output ---

    # Prepare the output line: distances for cities 1, 2, ..., N
    output = []
    for i in range(1, N + 1):
        # If distance[i] is still INF, it means the city is unreachable,
        # but the problem states all cities are reachable, so we just print distance[i].
        # However, for robustness, we can handle the case where the problem statement is ignored.
        # Since the constraint guarantees reachability, we just print the distance.
        output.append(str(distance[i]))

    # Print the final result separated by spaces
    sys.stdout.write(' '.join(output) + '\n')

if __name__ == "__main__":
    solve()