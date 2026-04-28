from collections import defaultdict, deque
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
ans = [0] * n
flag = True
q = deque()
for i in range(n):
    if ans[i] == 0:
        ans[i] = 1
        q.append(i)
        while q:
            top = q.popleft()
            for neighbor in graph[top]:
                if ans[neighbor] == ans[top]:
                    flag = False
                    break
                elif ans[neighbor] == 0:
                    ans[neighbor] = 3 - ans[top]
                    q.append(neighbor)
if not flag:
    print("IMPOSSIBLE")
else:
    print(*ans)













