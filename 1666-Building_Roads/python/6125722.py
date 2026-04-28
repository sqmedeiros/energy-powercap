from sys import stdin, stdout
input = stdin.readline
def print(*args, end='\n', sep=' ') -> None:
    stdout.write(sep.join(map(str, args)) + end)
def map_int():
    return map(int, input().split())
def list_int():
    return list(map(int, input().split()))
from collections import defaultdict

def dfs(start):

    stack = [start]
    while stack:
        node = stack.pop()
        visited[node] = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)


n, m = map_int()
graph = defaultdict(list)
visited = [0 for i in range(n+1)]
for i in range(m):
    n1, n2 = map_int()
    graph[n1].append(n2)
    graph[n2].append(n1)
components = 0
last = 0
ans = []
for i in range(1, n+1):
    if not visited[i]:
        if not last:
            last = i
        else:
            ans.append((last, i))
            last = i
        dfs(i)
        components += 1
print(components-1)
for i in ans:
    print(*i)

