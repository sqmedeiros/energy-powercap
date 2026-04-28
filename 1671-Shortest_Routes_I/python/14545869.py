# There are n cities and m flight connections between them. Your task is to determine the length of the shortest route from Syrjälä to every city.
# Input
# The first input line has two integers n and m: the number of cities and flight connections. The cities are numbered 1,2,\dots,n, and city 1 is Syrjälä.
# After that, there are m lines describing the flight connections. Each line has three integers a, b and c: a flight begins at city a, ends at city b, and its length is c. Each flight is a one-way flight.
# You can assume that it is possible to travel from Syrjälä to all other cities.
# Output
# Print n integers: the shortest route lengths from Syrjälä to cities 1,2,\dots,n.
# Constraints

# 1 \le n \le 10^5
# 1 \le m \le 2 \cdot 10^5
# 1 \le a,b \le n
# 1 \le c \le 10^9

# Example
# Input:
# 3 4
# 1 2 6
# 1 3 2
# 3 2 3
# 1 3 4

# Output:
# 0 5 2


import sys
import heapq

def main():
    # Read input
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])  # Number of cities
    m = int(data[1])  # Number of flights

    # Build adjacency list for the graph
    adj = [[] for _ in range(n + 1)]  # 1-based indexing
    idx = 2
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        adj[a].append((b, c))  # Flight from a to b with cost c
        idx += 3

    # Dijkstra's algorithm initialization
    dist = [float('inf')] * (n + 1)
    dist[1] = 0  # Distance to Syrjälä (city 1) is 0
    visited = [False] * (n + 1)
    heap = [(0, 1)]  # (distance, city)

    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, cost in adj[u]:
            if dist[v] > d + cost:
                dist[v] = d + cost
                heapq.heappush(heap, (dist[v], v))

    # Output shortest distances from Syrjälä to all cities
    print(' '.join(str(dist[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()