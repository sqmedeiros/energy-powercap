n, m = map(int, input().split())

rank = {node: 0 for node in range(1, n+1)}
parent = {node: node for node in range(1, n+1)}

def find(n):
    if parent[n]!=n:
        parent[n]=find(parent[n])
    return parent[n]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa==pb:
        return False
    if rank[pa]<rank[pb]:
        pa, pb = pb, pa
    parent[pb]=pa
    if rank[pa]==rank[pb]:
        rank[pa]+=1
    return True

for i in range(m):
    a, b = map(int ,input().split())
    union(a, b)

comps = set()
for i in range(1, n+1):
    comps.add(find(i))

need = len(comps)-1
print(need)

comps_list = list(comps)
for i in range(len(comps_list)-1):
    print(comps_list[i], comps_list[i+1])