import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
bosses = data[1:]

children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
 b = bosses[i - 2]
 children[b].append(i)

parent = [0] * (n + 1)
order = []
stack = [1]
parent[1] = -1

while stack:
 v = stack.pop()
 order.append(v)
 for c in children[v]:
  parent[c] = v
  stack.append(c)

sub = [1] * (n + 1)
for v in reversed(order):
 for c in children[v]:
  sub[v] += sub[c]

ans = [str(sub[i] - 1) for i in range(1, n + 1)]
sys.stdout.write(" ".join(ans))