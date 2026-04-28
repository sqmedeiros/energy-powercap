import sys
sys.setrecursionlimit(10**7)  # Increase the recursion limit

n = int(input())
adj_lst = [[] for i in range(n + 1)]
l = list(map(int, input().split()))

# Build adjacency list
for i in range(n - 1):
    adj_lst[l[i]].append(i + 2)

subordinates = [0] * n

def dfs(node, parent):
    subordinates[node - 1] = 1  # Initialize with 1 to count the node itself
    for neigh in adj_lst[node]:
        dfs(neigh, node)
        subordinates[node - 1] += subordinates[neigh - 1]

dfs(1, 1)  # Start DFS from the root node (node 1)

# Adjust counts to exclude the node itself from subordinates count
for i in range(n):
    subordinates[i] -= 1

print(*subordinates)