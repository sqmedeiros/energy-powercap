import sys

employee_count = int(sys.stdin.readline())

hierarchy = [[] for _ in range(employee_count)]

if employee_count > 1:
    boss_list = list(map(int, sys.stdin.readline().split()))
    for idx in range(employee_count - 1):
        worker_id = idx + 1
        boss_id = boss_list[idx] - 1
        hierarchy[boss_id].append(worker_id)

subtree_sizes = [0] * employee_count

dfs_stack = []
postorder_list = []
visited_nodes = [False] * employee_count

dfs_stack.append(0)

# Iterative DFS to generate post-order
while dfs_stack:
    current = dfs_stack[-1]

    if not visited_nodes[current]:
        visited_nodes[current] = True
        for child in reversed(hierarchy[current]):
            if not visited_nodes[child]:
                dfs_stack.append(child)
    else:
        dfs_stack.pop()
        postorder_list.append(current)

# Calculate subordinate counts bottom-up
for node in postorder_list:
    total_subordinates = 0
    for child in hierarchy[node]:
        total_subordinates += (1 + subtree_sizes[child])
    subtree_sizes[node] = total_subordinates

sys.stdout.write(" ".join(map(str, subtree_sizes)) + "\n")