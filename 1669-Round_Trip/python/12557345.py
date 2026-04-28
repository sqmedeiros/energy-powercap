from itertools import repeat
from sys import stdin, stdout
from array import array

buffer = stdin.buffer
write = stdout.write
n, m = map(int, buffer.readline().split())


arr = array("I", map(lambda x: int(x) - 1, buffer.read().split()))
g = [array("I") for _ in range(n)]

for i in range(0, 2 * m, 2):
    u, v = arr[i], arr[i + 1]
    g[u].append(v)
    g[v].append(u)

del arr


vrr = array("B", repeat(0, n))
prr = array("i", repeat(-1, n))
cs = ce = -1


def dfs(start):
    global cs, ce
    stk = [(start, -1)]
    while stk:
        u, p = stk.pop()
        vrr[u], prr[u] = 1, p
        for v in g[u]:
            if vrr[v] == 0:
                stk.append((v, u))
            elif vrr[v] == 1 and v != p:
                cs, ce = v, u
                return True
    return False


for i in range(n):
    if vrr[i] == 0:
        if dfs(i):
            crr = array("I")
            crr.append(cs + 1)
            u = ce
            cl = 0
            while u != cs:
                crr.append(u + 1)
                u = prr[u]
                cl += 1
            crr.append(cs + 1)
            write(f"{cl+2}\n")
            write(" ".join(map(str, reversed(crr))))
            break
else:
    write("IMPOSSIBLE")