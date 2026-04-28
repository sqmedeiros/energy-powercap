def process(G, n):
    g = {}
    for a, b in G:
        if a not in g:
            g[a] = []
        if b not in g:
            g[b] = []
        g[a].append(b)
        g[b].append(a)

    start = [1]
    d = {1: [0, None]}
    I = 1
    while len(start) > 0:
        next_s = set([])
        for x in start:
            if x in g:
                for y in g[x]:
                    if y not in d:
                        if y==n:
                            path = [y, x]
                            while path[-1] != 1:
                                path.append(d[path[-1]][1])
                            return [True, path[::-1]]
                        d[y] = [I, x]
                        next_s.add(y)
        I+=1
        start = next_s
    return [False, []]

n, m = [int(x) for x in input().split()]
G = []
for i in range(m):
    a, b = [int(x) for x in input().split()]
    G.append([a, b])
a1, a2 = process(G, n)
if a1:
    print(len(a2))
    print(' '.join(map(str, a2)))
else:
    print('IMPOSSIBLE')
