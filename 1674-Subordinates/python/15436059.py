import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
if n == 1:
    print(0)
    sys.exit()

boss = list(map(int, input().split()))

# Build children adjacency list
children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    children[boss[i - 2]].append(i)

subordinates = [0] * (n + 1)

# Iterative DFS (postorder)
stack = [(1, 0)]  # (node, state); state=0 means visit, 1 means process after children
order = []

while stack:
    node, state = stack.pop()
    if state == 0:
        stack.append((node, 1))
        for child in children[node]:
            stack.append((child, 0))
    else:
        total = 0
        for child in children[node]:
            total += 1 + subordinates[child]
        subordinates[node] = total

print(*subordinates[1:])

#end