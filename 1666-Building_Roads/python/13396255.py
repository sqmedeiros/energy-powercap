from collections import defaultdict, deque
read_int         = lambda: int(input())
read_str         = lambda: input().strip()
read_ints        = lambda: map(int, input().strip().split())
read_int_list    = lambda: list(map(int, input().strip().split()))

n, m = read_ints()
adj_list = defaultdict(list)
for _ in range(m):
    a, b = read_ints()
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False]*n
connected_comps = []

def bfs(city):
    if visited[city-1]:
        return []

    q = deque([city])
    comps = []
    while q:
        el = q.pop()
        comps.append(el)
        for n in adj_list[el]:
            if not visited[n - 1]:
                visited[n - 1] = True
                q.append(n)
    return comps

for city in range(1, n+1):
    comp =  bfs(city)
    if comp:
        connected_comps.append(comp)

print(len(connected_comps) - 1)
for i in range(len(connected_comps)-1):
    c1 = connected_comps[i]
    c2 = connected_comps[i+1]
    edge = [c1[0], c2[0]]
    print(c1[0], c2[0])