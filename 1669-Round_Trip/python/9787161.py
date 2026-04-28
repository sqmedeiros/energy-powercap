from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10000000)

def find_cycle(n, m, edges):
    # Create the graph
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Helper function to perform DFS and find the cycle
    def dfs(v, parent):
        visited[v] = True
        stack.append(v)
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                # Cycle detected
                cycle_start = neighbor
                cycle.append(cycle_start)
                while stack[-1] != cycle_start:
                    cycle.append(stack.pop())
                cycle.append(stack.pop())
                return True
        stack.pop()
        return False

    visited = [False] * (n + 1)
    stack = []
    cycle = []

    # Start DFS from each node
    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i, -1):
                cycle.reverse()
                return len(cycle), cycle

    return "IMPOSSIBLE"

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
edges = []
for i in range(m):
    a = int(data[2 + 2 * i])
    b = int(data[2 + 2 * i + 1])
    edges.append((a, b))

result = find_cycle(n, m, edges)

if result == "IMPOSSIBLE":
    print(result)
else:
    k, cycle = result
    print(k)
    print(" ".join(map(str, cycle)))