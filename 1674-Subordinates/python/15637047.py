import sys

input = sys.stdin.readline

n = int(input())
bosses = list(map(int, input().split()))

tree = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    tree[bosses[i - 2]].append(i)

sub = [0] * (n + 1)

stack = [(1, 0)]
while stack:
    u, state = stack.pop()
    if state == 0:
        stack.append((u, 1))
        for v in tree[u]:
            stack.append((v, 0))
    else:
        total = 0
        for v in tree[u]:
            total += sub[v] + 1
        sub[u] = total

print(*sub[1:])