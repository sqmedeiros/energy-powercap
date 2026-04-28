n,m = map(int, input().split())

# if parents[u] = v then u,v are connected by an edge and u < v
parents = [-1 for _ in range(n)]

def head(u, parents):
    while parents[u] != -1:
        u = parents[u]
    return u

def collapse(u, u_head):
    while u != u_head:
        tmp = u
        parents[u] = u_head
        u = parents[tmp]

for _ in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    # merge components
    u_head, v_head = head(u, parents), head(v, parents)
    # if u_head = v_head then nothing to merge
    if u_head != v_head:
        parents[min(u_head,v_head)] = max(v_head,u_head)
    collapse(u, u_head)
    collapse(v, v_head)

roads = []
i_prev = -1
for i in range(n):
    if parents[i] == -1:
        if i_prev != -1:
            roads.append((i_prev, i))
        i_prev = i

print(len(roads))
for u,v in roads:
    print(u+1,v+1)