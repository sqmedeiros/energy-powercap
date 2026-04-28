
import heapq
from typing import List, Tuple, Dict, Iterator

INF = float('inf')


def dijkstra_sol(num_vert: int, adj_list: List[List[Tuple[int, int]]]):
    dist = [INF for _ in range(num_vert + 1)]
    # pred = [-1 for _ in range(num_vert + 1)]
    visited = [False for _ in range(num_vert + 1)]

    min_heap = []

    dist[1] = 0  # Start at city 1
    heapq.heappush(min_heap, (0, 1))

    while len(min_heap) > 0:
        _, v = heapq.heappop(min_heap)
        if visited[v]:
            continue
        visited[v] = True

        for u, weight in adj_list[v]:
            if dist[v] + weight < dist[u]:  # If edge v->u is tense...
                dist[u] = dist[v] + weight  # relax that edge.
                heapq.heappush(min_heap, (dist[u], u))

    for i in range(1, num_vert + 1):
        print(dist[i], end=" ")


def input_line_ints() -> Iterator[int]:
    return map(int, input().strip().split())


if __name__ == "__main__":
    n, m = input_line_ints()

    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = input_line_ints()
        adj_list[a].append((b, c))

    dijkstra_sol(n, adj_list)