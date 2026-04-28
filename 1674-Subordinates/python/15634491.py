n = int(input())
bosses = list(map(int, input().split()))
children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    children[bosses[i - 2]].append(i)

subordinates = [0] * (n + 1)
stack = [(1, 0)]  

while stack:
    node, state = stack.pop()

    if state == 0:
        stack.append((node, 1))
        for child in children[node]:
            stack.append((child, 0))
    else:
        total = 0
        for child in children[node]:
            total += subordinates[child] + 1
        subordinates[node] = total

print(" ".join(map(str, subordinates[1:])))