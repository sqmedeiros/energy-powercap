import heapq
from collections import deque


from collections import deque
class BeingZero:
    def solve(self, edges, n, m):
        #write your code here
        dis = [float('inf') for i in range(n+1)]
        par = [-1 for i in range(n+1)]
        dis[1] = 0
        adj = [[] for i in range(n+1)]
        for ed in edges:
            u,v = ed
            adj[u].append(v)
            adj[v].append(u)
        vis = set()
        q = deque()
        q.append(1)
        vis.add(1)
        while (len(q)>0):
            x = q.popleft()
            for ch in adj[x]:
                if(dis[ch]>dis[x]+1):
                    dis[ch] = dis[x]+1
                    par[ch] = x
                    q.append(ch)
        if(dis[n]==float('inf')):
            return []
        else:
            ans = [n]
            val = n

            while(par[val]!=-1):
                ans.append(par[val])
                val = par[val]
            return ans[::-1]








if __name__ == "__main__":
    t =1
    solver = BeingZero()

    for _ in range(t):
        n, m = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        result = solver.solve(edges, n, m)

        if not result:
            print("IMPOSSIBLE")
        else:
            print(len(result))
            print(" ".join(map(str, result)))