import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

alist = [[] for _ in range(n+1)]
team = [0]*(n+1)

# 生成邻接表
for _ in range(m):
    a, b = map(int, input().split())
    alist[a].append(b)
    alist[b].append(a)

def dfs(i):
    for j in alist[i]:
        if team[j]:
            if team[j] == team[i]:
                print('IMPOSSIBLE')
                exit()
        else:
            team[j] = 3 - team[i] # 等价于team[j] = 1 if team[i] == 1 else 1
            dfs(j)

for i in range(1, n+1):
    if not team[i]:
        team[i] = 1
        dfs(i)

print(*team[1:])