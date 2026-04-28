import sys
sys.setrecursionlimit(10**9)

n = int(input())
c = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
sub = []

for i in range(2,n+1):
    sub.append(i)

for i in range(n-1):
    adj[c[i]].append(sub[i])

memo = {}
visited = [False for _ in range(n + 1)]

def count_subordinates(s):
    if s in memo:
        return memo[s]
    visited[s] = True
    total_sub = 0 
    for j in adj[s]:
        total_sub += 1 + count_subordinates(j) 
    memo[s] = total_sub
    return total_sub

results = [0] * (n + 1)  
for i in range(1, n + 1):
    results[i] = count_subordinates(i)

results = results[1:]

print(' '.join(map(str,results)))
