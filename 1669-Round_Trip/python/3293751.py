from sys import setrecursionlimit, stdout, stdin

setrecursionlimit(10 ** 6)


def dfs(node, par):
    v[node] = 1
    ans.append(node)
    for i in adj[node]:
        if not v[i]:
            if dfs(i, node):
                return True
        else:
            if i != par:
                ans.append(i)
                return True
    ans.pop()
    return False


n, m = stdin.readline().split()
n = int(n)
m = int(m)
adj = {i + 1: [] for i in range(n)}
v = [0] * (n + 1)
for i in range(m):
    a, b = stdin.readline().split()
    a = int(a)
    b = int(b)
    adj[a].append(b)
    adj[b].append(a)

ans = []
flag = False
for i in range(n):
    if not v[i] and dfs(i + 1, 0):
        flag = True
        break
c = 0
fans = []
if flag:
    c += 1
    t = ans.pop()
    fans.append(t)
    while ans[-1] != t:
        c += 1
        fans.append(ans.pop())
    fans.append(t)
    c += 1
    stdout.write(str(c) + '\n')
    for i in fans:
        stdout.write(str(i) + ' ')
else:
    stdout.write("IMPOSSIBLE")