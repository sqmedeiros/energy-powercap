from collections import defaultdict, deque

n = int(input())
parent = list(map(int, input().split()))

children = defaultdict(list)
for i, p in enumerate(parent, start=2):
    children[p].append(i)

result = [0] * (n + 1)

stack = [(1, 0)]
visited = [False] * (n + 1)

while stack:
    node, state = stack.pop()
    if state == 0:
        stack.append((node, 1))
        for child in children[node]:
            stack.append((child, 0))
    else:
        total = 0
        for child in children[node]:
            total += 1 + result[child]
        result[node] = total

print(' '.join(map(str, result[1:])))