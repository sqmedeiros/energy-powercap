n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

v = [0] * (n + 1)
p = [0] * (n + 1)

for s in range(1, n + 1):
    if v[s]: continue
    st = [(s, -1)]
    while st:
        x, pr = st.pop()
        if v[x] == 0:
            v[x] = 1
            p[x] = pr
            st.append((x, -2))
            for y in g[x]:
                if y == pr: continue
                if v[y] == 0: st.append((y, x))
                elif v[y] == 1:
                    c = [y]
                    z = x
                    while z != y:
                        c.append(z)
                        z = p[z]
                    c.append(y)
                    c.reverse()
                    print(len(c))
                    print(*c)
                    exit()
        elif v[x] == 1 and pr == -2:
            v[x] = 2
print("IMPOSSIBLE")