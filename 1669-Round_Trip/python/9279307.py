def find_round_trip(n, m, roads):
    from sys import setrecursionlimit, stdin, stdout
    import collections
    import sys
    input = stdin.read
    setrecursionlimit(10**6)

    data = input().split()
    n = int(data[0])
    m = int(data[1])
    adj = collections.defaultdict(list)

    index = 2
    for _ in range(m):
        a = int(data[index])
        b = int(data[index+1])
        adj[a].append(b)
        adj[b].append(a)
        index += 2

    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    cycle_start = -1
    cycle_end = -1

    def dfs(v):
        nonlocal cycle_start, cycle_end
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                parent[neighbor] = v
                if dfs(neighbor):
                    return True
            elif neighbor != parent[v]:
                cycle_start = neighbor
                cycle_end = v
                return True
        return False

    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i):
                break

    if cycle_start == -1:
        print("IMPOSSIBLE")
    else:
        cycle = []
        cycle.append(cycle_start)
        v = cycle_end
        while v != cycle_start:
            cycle.append(v)
            v = parent[v]
        cycle.append(cycle_start)
        cycle.reverse()
        print(len(cycle))
        print(" ".join(map(str, cycle)))

# Example usage:
# Assuming the input is provided in the expected format via standard input
find_round_trip(0, 0, []) # Note: Actual input should be read as per the function requirements