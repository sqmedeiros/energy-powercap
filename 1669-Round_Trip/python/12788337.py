def chinh(n,danh):
    visited = [False]*(n+1)
    tv = [0]*(n+1)
    for i in range(1,n+1):
        if not visited[i]:
            stack = [(i,0)]
            visited[i] = True
            while stack:
                u , idx = stack[-1]
                if idx < len(danh[u]):
                    v = danh[u][idx]
                    stack[-1] = (u,idx+1)
                    if v != tv[u]:
                        if visited[v]:
                            da = [v]
                            a = u
                            while a != v and a != 0:
                                da.append(a)
                                a = tv[a]
                            da.append(v)
                            print(len(da))
                            print(*da)
                            return
                        else:
                            visited[v] = True
                            tv[v] = u
                            stack.append((v,0))
                else:
                    stack.pop()
    print('IMPOSSIBLE')
    return
n , m = map(int,input().split())
danh = [[] for _ in range(n+1)]
for _ in range(m):
    a , b = map(int,input().split())
    danh[a].append(b)
    danh[b].append(a)
chinh(n,danh)