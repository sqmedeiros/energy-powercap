# import sys
# import os

# # Change to the directory containing input.txt
# os.chdir('Graph Algorithms/Task 1668 - Building Teams')

# # Redirect stdin and stdout
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

def main():
    import sys
    input = sys.stdin.readline # ChatGPT Optimisation
    n, m = map(int, input().split())
    from collections import defaultdict
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    from collections import deque
    visited = [False]*n
    for start in range(n):
        if not visited[start]:
            q = deque([start+1])
            visited[start] = 1
            while q:
                node = q.popleft()
                for nbr in graph[node]:
                    if not visited[nbr-1]:
                        visited[nbr-1] = 2 if visited[node-1] == 1 else 1
                        q.append(nbr)
                    elif visited[nbr-1] == visited[node-1]:
                        print('IMPOSSIBLE')
                        return
    print(*visited)
    return
if __name__ == "__main__":
    main()