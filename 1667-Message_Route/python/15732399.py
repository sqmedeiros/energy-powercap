# bfs
import collections
import sys
sys.setrecursionlimit(200000)

def solve():
    input = sys.stdin.read
    data = input().split()
    iterator = iter(data)

    # num_test_cases = int(next(iterator))
    # for _ in range(num_test_cases):
    n=int(next(iterator))
    m=int(next(iterator))
    level=[0]*(n+1)
    adj_list = [[] for _ in range(n+1)]
    for i in range (m):
        u=int(next(iterator))
        v=int(next(iterator))
        adj_list[u].append(v)
        adj_list[v].append(u)
    visted=[0]*(n+1)
    level=[float('-inf')]*(n+1)
    def bfs(source):
        q=collections.deque()
        q.append(source)
        visted[source]=1
        level[source]=0
        # route=[source]
        parents=[0]*(n+1)
        while(q):
            cur_v=q.popleft()
            for child in adj_list[cur_v]:
                if visted[child]==1: continue
                # route.append(child)
                if child==n: 
                    route=[n]
                    par=cur_v
                    while(par!=1):
                        route.append(par)
                        par=parents[par]
                    route.append(1)
                    print(len(route))
                    print(*route[::-1])
                    sys.exit(0)
                parents[child]=cur_v
                q.append(child)
                visted[child]=1
                level[child]=level[cur_v]+1

    bfs(1)
    print("IMPOSSIBLE")

solve()

