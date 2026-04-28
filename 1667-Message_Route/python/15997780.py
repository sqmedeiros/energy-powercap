import sys
from collections import deque

sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.read().split()

    if not input :
        return

    iterator=iter(input)

    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj=[[] for _ in range(n+1)]
    for _ in range (m):
        u = int(next(iterator))
        v= int (next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    queue=deque([1])
    parent = [0] * (n+1)
    parent [1]=-1
    found = False

    while queue:
        curr = queue.popleft()

        if curr == n:
            found = True
            break
        for susjed in adj[curr]:
            if parent[susjed]==0:
                parent[susjed]=curr
                queue.append(susjed)

    if found:
        path= []
        curr=n

        while curr !=-1:
            path.append(curr)
            curr = parent[curr]

        path.reverse()

        print(len(path))
        print(*path)

    else:
        print("IMPOSSIBLE")

if __name__=="__main__":
    solve()