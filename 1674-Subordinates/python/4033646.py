# 2022-06-04
# Subordinates

# Option 1: brute force
# for each employee, walk up tree until hit CEO
# O(N^2)

# Option 2:
# BFS from CEO to find distances to each employee
# sort in decreasing order of dist to CEO
# num subordinates = sum of num subordinates of each direct report + 1
# O(N log N)

from collections import deque

def calc_dist(start_node, N, adj):
    """Return list of distances"""

    distances = [None] * N
    visited = [False] * N

    queue = deque()

    # node, dist
    queue.append((start_node, 0))
    visited[start_node] = True
    while queue:
        cur, dist = queue.popleft()

        distances[cur] = dist

        for neigh in adj[cur]:
            if not visited[neigh]:
                visited[neigh] = True
                queue.append((neigh, dist+1))

    return distances

def main():
    N = int(input())
    bosses = list(map(int, input().split(" ")))

    adj = []
    for i in range(N):
        adj.append([])

    for idx, boss in enumerate(bosses):
        adj[boss-1].append(idx+1)


    distances = calc_dist(0, N, adj)

    locs = [
        (dist, idx)
        for idx, dist in enumerate(distances)
    ]

    locs = sorted(locs, key=lambda v: v[0], reverse=True)


    num_sub = [0] * N
    for dist, idx in locs:

        subtree_sum = sum(
            num_sub[sub]
            for sub in adj[idx]
        )

        num_sub[idx] = subtree_sum + 1


    print(
        " ".join(
            str(val - 1)
            for val in num_sub
        )
    )


if __name__ == "__main__":
    main()