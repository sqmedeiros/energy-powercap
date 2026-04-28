from collections import deque

# Read input
def main():
    n, m = map(int, input().split())

    teams = [0] * (n + 1)

    # Initialize adjacency list
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # BFS to assign teams
    for i in range(1, n + 1):
        if teams[i] == 0:
            teams[i] = 1
            queue = deque([i])

            while queue:
                current = queue.popleft()

                for neighbor in graph[current]:
                    if teams[neighbor] == 0:
                        teams[neighbor] = 3 - teams[current]
                        queue.append(neighbor)
                    elif teams[neighbor] == teams[current]:
                        print("IMPOSSIBLE")
                        return

    # Prepare and print the output
    print(" ".join(map(str, teams[1:])))

if __name__ == "__main__":
    main()