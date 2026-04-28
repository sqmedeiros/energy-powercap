import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
aux = list(map(int, input().split()))

for i in range(2, n + 1):
    adj[aux[i - 2]].append(i)

a = [0] * (n + 1)

stack = [(1, 0)]
while stack:
    v, state = stack.pop()
    if state == 0:
        stack.append((v, 1))
        for u in adj[v]:
            stack.append((u, 0))
    else:
        total = 0
        for u in adj[v]:
            total += a[u] + 1
        a[v] = total

sys.stdout.write(' '.join(map(str, a[1:])) + '\n')