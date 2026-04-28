import sys

inp = iter(sys.stdin.buffer.read().split())
n, m = [int(next(inp)) for _ in range(2)]
groups = [0] * n
groups[0]
dd = {}
for _ in range(m):
    a, b = [int(next(inp)) for _ in range(2)]
    if a in dd:
        dd[a].add(b)
    else:
        dd[a] = {b}
    if b in dd:
        dd[b].add(a)
    else:
        dd[b] = {a}

not_team_one = set()
not_team_two = set()
for i in range(1, n + 1):
    if groups[i - 1] == 0:
        groups[i - 1] = 1
        stack = [i]
        while stack:
            node = stack.pop()
            node_group = groups[node - 1]
            for child in dd.get(node, []):
                if groups[child - 1] != 0:
                    if groups[child - 1] == node_group:
                        sys.stdout.write('IMPOSSIBLE\n')
                        sys.exit()
                    else:
                        continue
                if node_group == 1:
                    groups[child - 1] = 2
                else:
                    groups[child - 1] = 1
                stack.append(child)

out = ' '.join([str(c) for c in groups])
sys.stdout.write(f'{out}\n')