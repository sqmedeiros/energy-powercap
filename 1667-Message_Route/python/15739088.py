from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

prev = [-1] * n
queue = deque([0])
while queue:
    cur = queue.popleft()
    for nb in adj[cur]:
        if prev[nb] == -1:
            prev[nb] = cur
            queue.append(nb)
        if nb == n - 1:
            queue.clear()

if prev[-1] == -1:
    print("IMPOSSIBLE")
else:
    cur = n - 1
    ans = []
    while cur:
        ans.append(cur + 1)
        cur = prev[cur]
    print(len(ans) + 1)
    print(1, *ans[::-1])