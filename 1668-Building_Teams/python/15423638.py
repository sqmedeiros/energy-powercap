import sys

# Increase recursion depth just in case, though we rely on stack
sys.setrecursionlimit(200000)

def solve():
    # Fast I/O
    input = sys.stdin.readline

    try:
        line = input().split()
        if not line: return
        n, m = map(int, line)
    except ValueError:
        return

    # Build Adjacency List
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # Array to store team assignments. 
    # 0 = unassigned, 1 = Team 1, 2 = Team 2
    teams = [0] * (n + 1)

    # Iterate through all students to handle disconnected components
    for i in range(1, n + 1):
        if teams[i] == 0:
            # Start a new component, assign first person to Team 1
            teams[i] = 1
            stack = [i]

            while stack:
                u = stack.pop()

                # Determine what the enemy team is
                # If u is 1, enemy is 2. If u is 2, enemy is 1.
                enemy_team = 3 - teams[u]

                for v in adj[u]:
                    if teams[v] == 0:
                        # If neighbor is unvisited, assign them to enemy team
                        teams[v] = enemy_team
                        stack.append(v)
                    elif teams[v] == teams[u]:
                        # Conflict found: Neighbor is on the same team!
                        print("IMPOSSIBLE")
                        return

    # If we made it here, a solution was found.
    # Print the array from index 1 to n
    print(*teams[1:])

if __name__ == "__main__":
    solve()