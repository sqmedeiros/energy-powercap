from collections import deque

n = int(input())

result = [0]*n
adj = [[] for x in range(n)]

inp = input().split()
for i in range(n-1):
    adj[int(inp[i])-1].append(i+1)

q = deque()
stack = [0]
q.append(0)

while q:
    curr = q.pop()
    for ele in adj[curr]:
        q.appendleft(ele)
        stack.append(ele)

for i in range(n-1,-1,-1):
    for ele in adj[stack[i]]:
        result[stack[i]]+=result[ele]+1

print(*result)