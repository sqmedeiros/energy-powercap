import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
parent = [0] * (n + 1)
cycle = []

def dfs(u, p):
    visited[u] = True
    for v in graph[u]:
        if v == p:#לא לחזור אחורה לצומת שממנו באנו
            continue
        if visited[v]:#מצאנו צומת שכבר היינו בו
            path = [u]#נתחיל בשמירת המסלול, הסדר לא משנה,אנחנו מחליטים מי הראשון/אחרון
            cur = u
            while cur != v:
                cur = parent[cur]
                path.append(cur)
            path.append(u)  # לסגור את המעגל
            cycle.extend(reversed(path))#אולי כדאי מראש להכניס הפוך, בדיקיו כדי להפחית סיבוכיות
            return True
        else:
            parent[v] = u
            if dfs(v, u):
                return True
    return False

found = False
for i in range(1, n + 1):
    if not visited[i]:
        if dfs(i, -1):
            found = True
            break

if found:
    print(len(cycle))
    print(" ".join(map(str, cycle)))
else:
    print("IMPOSSIBLE")