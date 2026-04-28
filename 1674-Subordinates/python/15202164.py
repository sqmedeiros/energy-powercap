import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit()

boss = list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    tree[boss[i - 2]].append(i)

subordinates = [0] * (n + 1)
stack = [(1, 0)]
order = []

while stack:
    node, visited = stack.pop()
    if visited:
        for child in tree[node]:
            subordinates[node] += 1 + subordinates[child]
    else:
        stack.append((node, 1))
        for child in tree[node]:
            stack.append((child, 0))

print(*subordinates[1:])