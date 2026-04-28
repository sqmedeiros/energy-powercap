# Determine if a graph is bipartite and return the coloring of the nodes if it is 
# (if students can be divided without being friends with each other)

def bipartite_graph(n, connections):
    adj = [[] for _ in range(n + 1)]
    for a, b in connections:
        adj[a].append(b)
        adj[b].append(a)

    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]
                        stack.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return "IMPOSSIBLE"

    return color[1:]

def main():
    n, m = map(int, input().split())
    connections = [tuple(map(int, input().split())) for _ in range(m)]

    result = bipartite_graph(n, connections)
    if result == "IMPOSSIBLE":
        print(result)
    else:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()