from collections import deque

def main():
    n, m = tuple(map(int, input().split(" ")))
    adj = [[] for _ in range(n)]
    parents = [None for _ in range(n)]
    for _ in range(m):
        a, b = tuple(map(lambda x: int(x)-1, input().split(" ")))
        adj[a].append(b)
        adj[b].append(a)

    q = deque()
    q.append(0)
    parents[0] = 0
    while q:
        a = q.popleft()
        for b in adj[a]:
            if parents[b] == None:
                parents[b] = a
                if b == n - 1:
                    break 
                q.append(b)
    if parents[n-1] != None:
        curr = n-1
        path = [n]
        while curr != 0:
            path.append(parents[curr] + 1)
            curr = parents[curr]
        path.reverse()
        print(len(path))
        print(" ".join(map(str,path)))
    else:
        print("IMPOSSIBLE")




main()