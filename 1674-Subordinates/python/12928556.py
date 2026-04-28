import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
bosses = list(map(int, sys.stdin.readline().split()))

subordinates = [[] for _ in range(n)]
for i, b in enumerate(bosses, start=2):
    subordinates[b-1].append(i-1)

result = [0]*n

def dfs(u):
    count = 0
    for v in subordinates[u]:
        count += 1 + dfs(v)
    result[u] = count
    return count

dfs(0)
print(*result)