n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
team = [0] * (n+1)

# Read friendships
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Iterative DFS function
def dfs(start):
    stack = [(start, 1)]
    while stack:
        node, c = stack.pop()
        if team[node] == c:
            continue
        if team[node] == 3 - c:
            return False
        team[node] = c
        for friend in graph[node]:
            if team[friend] == 0:
                stack.append((friend, 3 - c))
    return True

# Main loop to start DFS
for i in range(1, n+1):
    if team[i] == 0 and not dfs(i):
        print("IMPOSSIBLE")
        exit(0)

print(" ".join(map(str, team[1:])))