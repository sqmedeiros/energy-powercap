import sys
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.read().split()

    if not input:
        return

    iterator=iter(input)
    try:
        n = int (next(iterator))
        m=int (next(iterator))
    except StopIteration:
        return

    adj=[[] for _ in range (n+1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n+1)
    parent = [0] * (n+1)

    cycle_start= -1
    cycle_end=-1

    def dfs(u, p):
        nonlocal cycle_start, cycle_end
        visited[u]=True
        parent[u]=p

        for v in adj[u]:
            if v==p:
                continue

            if visited[v]:
              cycle_start=v
              cycle_end=u
              return True

            if not visited[v]:
              if dfs(v, u):
               return True
        return False

    found = False
    for i in range (1, n+1):
       if not visited[i]:
          if dfs(i, -1):
             found = True
             break

    if found:
       path=[]
       curr=cycle_end

       while curr !=cycle_start:
          path.append(curr)
          curr = parent[curr]
       path.append(cycle_start)
       path.append(cycle_end)
       print(len(path))
       print(*path)

    else:
       print("IMPOSSIBLE")
if __name__=="__main__":
   solve()
