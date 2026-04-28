from collections import deque



from collections import deque

def helper(n, m, adj_list):
    q = deque()
    visited = set()
    visited.add(1)

    q.append((1, 1))          # step = 0
    parent = {1: None}

    while q:
        node, step = q.popleft()

        if node == n:
            print(step)

            # reconstruct path
            path = []
            curr = n
            while curr is not None:
                path.append(curr)
                curr = parent[curr]

            print(*path[::-1])
            return

        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                q.append((neighbor, step + 1))


    print("IMPOSSIBLE")




if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_list = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)  


    helper(n, m, adj_list)
