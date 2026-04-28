def dfs(node):
    path[node] = -1
    st = [[node,-1]]
    while len(st):
        el,par = st.pop()
        vis[el] = 1
        # print(el, par)
        for i in adj[el]:
            # print("x", i, par)
            if i == par:
                continue
            path[i] = el 
            if vis[i]:
                return i

            st.append([i,el])


n,m = map(int, input().split())
adj = [[] for i in range(n)]
for i in range(m):
    x,y = map(int, input().split())
    adj[x-1].append(y-1)
    adj[y-1].append(x-1)
vis = [False for i in range(n)]
path = [-1 for i in range(n)]
flg = -1
for i in range(n):
    if vis[i]:
        continue
    flg = dfs(i)
    if flg != None:
        break
# print(path,flg)
if flg != None:
    tmp = flg
    ans = [tmp+1]
    tmp = path[tmp]
    while tmp != flg:
        ans.append(tmp+1)
        tmp = path[tmp]
    ans.append(flg+1)
    print(len(ans))
    print(*ans)

else:
    print("IMPOSSIBLE")