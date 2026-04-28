from collections import defaultdict
n = int(input())
rel = list(map(int , input().split()))
adj = defaultdict(list)
for i in range(2 , n + 1):
    adj[rel[i - 2]].append(i)
stack = []
stack.append((1 , False))
ans = [0] * (n + 1)
while stack:
    node , vis = stack.pop()
    if not vis:
        stack.append((node , True))
        for i in adj[node]:
            stack.append((i , False))
    else:
        for c in adj[node]:
            ans[node] += 1 +ans[c]
print(*ans[1:])

#Intuition and Explanation
"""
1. Indexing starts from 2 to n, value at index indicates
the superior.
2. Building an adj list helps to keep track of subordinates.
"""