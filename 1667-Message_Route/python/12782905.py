def chinh(n,danh):
    deque = [(1 , 1)]
    visited = [False]*(n+1)
    tv = [0]*(n+1)
    while deque:
        x , y  = deque.pop(0)
        if x == n:
            print(y)
            da = [n]
            while tv[x] != 1:
                da.append(tv[x])
                x = tv[x]
            da.append(1)
            da = da[::-1]
            print(*da)
            return
        if danh[x]:
            for u in danh[x]:
                if not visited[u]:
                    deque.append((u,y+1))
                    visited[u] = True
                    tv[u] = x
    print('IMPOSSIBLE')
    return
n , m = map(int,input().split())
danh = [[] for _ in range(n+1)]
for _ in range(m):
    a , b = map(int,input().split())
    danh[a].append(b)
    danh[b].append(a)
chinh(n,danh)