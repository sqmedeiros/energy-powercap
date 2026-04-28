import sys
input = sys.stdin.readline

N = int(input())
boss = list(map(int, input().split()))

tree = [[] for _ in range(N + 1)]

for i in range(2, N + 1):
    tree[boss[i - 2]].append(i)

subordinates = [0] * (N + 1)

stack = []
order = []

stack.append(1)
while stack:
    node = stack.pop()
    order.append(node)
    for child in tree[node]:
        stack.append(child)

for node in reversed(order):
    for child in tree[node]:
        subordinates[node] += 1 + subordinates[child]

print(' '.join(map(str, subordinates[1:])))