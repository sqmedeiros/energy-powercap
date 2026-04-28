from collections import deque

# Read input
n = int(input())
if n > 1:
    bosses = list(map(int, input().split()))
else:
    bosses = []

# Initialize parent array
parent = [0] * (n + 1)
for i in range(2, n + 1):
    parent[i] = bosses[i - 2]

# Build the tree (list of subordinates for each employee)
tree = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    tree[parent[i]].append(i)

# Initialize unprocessed children count and answer array
unprocessed = [len(tree[i]) for i in range(n + 1)]
ans = [0] * (n + 1)

# Initialize queue with leaves
queue = deque()
for i in range(1, n + 1):
    if unprocessed[i] == 0:
        queue.append(i)

# Process the queue
while queue:
    u = queue.popleft()
    if parent[u] > 0:  # If u has a parent
        p = parent[u]
        ans[p] += 1 + ans[u]  # Add u and its subordinates to p’s count
        unprocessed[p] -= 1
        if unprocessed[p] == 0:
            queue.append(p)

# Output the number of subordinates for each employee
print(' '.join(map(str, ans[1:n+1])))