import sys
sys.setrecursionlimit(100000000)
n = int(input())
l = [int(i)-1 for i in input().split()]
l = [-1] + l
g = [[] for i in range(n)]
for i in range(1,n):
    g[l[i]].append(i)
tps = []
visited = [-1 for i in range(n)]
visited[0] = 1
q = [0]
while len(q)!= 0:
    to_pop = True
    curr = q[-1]
    for i in g[curr]:
        if visited[i] == -1:
            q.append(i)
            to_pop = False
            visited[i] = 1
    if to_pop:
        rem = q.pop()
        tps.append(rem)
# print(tps)       
ans = [0 for i in range(n)]
for i in tps:
    for j in g[i]:
        ans[i] += 1 + ans[j]
print(" ".join([str(i) for i in ans]))