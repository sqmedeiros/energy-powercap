n, m = list(map(int, input().split()))

adj = [[] for _ in range(n+1)]
vis = [False for _ in range(n+1)]
pai = [None for _ in range(n+1)]
team = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)
for i in range(1,n+1):
    if not vis[i]:
        cur = i
        vis[cur] = True
        team[cur] = 1
        while True:
            flag = True
            for ad in adj[cur]:
                if vis[ad]:
                    if team[ad] == team[cur]:
                        print('IMPOSSIBLE')
                        exit()
                else:
                    vis[ad] = True
                    flag = False
                    pai[ad] = cur
                    team[ad] = 1 if team[cur] == 2 else 2
                    cur = ad
                    break
            if flag:
                if cur == i: break
                cur = pai[cur]

for i in range(1, len(team)):
    print(team[i], end=' ')
print()
