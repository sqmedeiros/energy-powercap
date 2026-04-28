import collections


def check(v, color,adj):
    q = collections.deque()
    q.append(v)
    color[v] = 0
    while q:
        node = q.popleft()
        for u in adj[node]:
            if color[u] == -1:
                color[u] = not color[node]
                q.append(u)
            elif color[u] == color[node]:
                return False

    return True


if __name__ == "__main__":
    v, e = map(int, input().split())
    adj = {}
    for i in range(v+1):
        adj[i] = []
    for i in range(e):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    flag = 0
    color = [-1]*(v+1)
    for i in range(1, v+1):
        if color[i] == -1:
            if not check(i, color,adj):
                flag = 1
                print("IMPOSSIBLE")
                break

    if not flag:
        for i in range(1, v+1):
            if color[i] == 0:
                print(1, end=" ")
            else:
                print(2, end=" ")
