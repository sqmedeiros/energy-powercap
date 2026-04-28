#import io,os
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import sys
from collections import deque

n,m = [int(i) for i in input().split()]
adj = [[] for i in range(n+1)]
for i in range(m):
    a,b = [int(i) for i in input().split()]
    adj[a].append(b)
    adj[b].append(a)

prev = [0 for i in range(n+1)]
for j in range(1, n+1):
    if not prev[j]:
        prev[j] = -1
        Q = deque([j])
        while len(Q):
            v = Q.popleft()
            for u in adj[v]:
                if not prev[u]:
                    Q.append(u)
                    prev[u] = v
                else:
                    if u != prev[v]:
                        #found an answer!!
                        path1 = [u]
                        while prev[u] != -1:
                            u = prev[u]
                            path1.append(u)
                        spath1 = [False for i in range(n+1)]
                        for i in path1:
                            spath1[i] = True
                        path2 = [v]
                        while (prev[v] != -1) and (not spath1[v]):
                            v = prev[v]
                            path2.append(v)
                        if spath1[path2[0]]:
                            #v is on the path lol
                            x = path1.index(v)
                            print(x+2)
                            path1 = [v] + path1[:x+1]
                            sys.stdout.write(" ".join(map(str,path1)) + "\n")
                            exit()
                        elif path1[0] in path2:
                            #u is on the path lol
                            x = path2.index(u)
                            print(x+2)
                            path2 = [u] + path2[:x+1]
                            sys.stdout.write(" ".join(map(str,path2)) + "\n")
                            exit()
                        else:
                            s = []
                            x = path1.index(path2[-1])
                            s = [path1[0]]
                            s += path2
                            s.pop()
                            s += path1[:x+1][::-1]
                            print(len(s))
                            sys.stdout.write(" ".join(map(str,s)) + "\n")
                            exit()


print('IMPOSSIBLE')
