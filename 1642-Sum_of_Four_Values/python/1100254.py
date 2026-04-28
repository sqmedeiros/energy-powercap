n, s = map(int, input().split())
a = [int(x) for x in input().split()]
f = {}
for x in a:
    f[x] = f.get(x, 0) + 1

b = list(f.keys())
p = {}
for i in range(len(b)):
    for j in range(i + 1, len(b)):
        k = b[i] + b[j]
        if k not in p:
            p[k] = []
        if len(p[k]) >= 3: continue
        p[k].append((b[i], b[j]))


def get_indecies(t):
    z = list(t)
    for j in range(4):
        for i in range(n):
            if z[j] == a[i]:
                z[j] = i + 1
                a[i] = 0
                break
    return z


def fun():
    if n < 4: return None

    if s % 4 == 0 and f.get(s // 4, 0) >= 4:
        return [s // 4] * 4

    for x in a:
        if s != 4 * x and f[x] >= 3 and s - 3 * x in f:
            return [s - 3 * x] + [x] * 3

    for x in a:
        if f[x] < 2: continue
        y = (s - 2 * x) // 2
        if s == 2 * (x + y) and x != y and f.get(y, 0) > 1:
            return [x, x, y, y]
        if s - 2 * x in p:
            for i, j in p[s - 2 * x]:
                if i != x and j != x:
                    return [x, x, i, j]

    for x in p:
        if s - x in p:
            for i1, j1 in p[x]:
                for i2, j2 in p[s - x]:
                    if i1 != i2 and i1 != j2 and j1 != i2 and j1 != j2:
                        return [i1, j1, i2, j2]

    return None


r = fun()
if r is None:
    print('IMPOSSIBLE')
else:
    print(*get_indecies(r))